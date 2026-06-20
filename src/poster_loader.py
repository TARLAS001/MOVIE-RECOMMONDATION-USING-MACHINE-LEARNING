"""
Poster Loading Module - Handles TMDB API poster fetching with retry logic
"""

import requests
import streamlit as st
from typing import Optional
import time
from functools import wraps

class PosterLoaderConfig:
    """Configuration for poster loading"""
    MAX_RETRIES = 3
    TIMEOUT = 5
    RETRY_DELAY = 1
    FALLBACK_IMAGE = "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"
    FALLBACK_IMAGE_ERROR = "https://placehold.co/500x750/FF6B6B/FFFFFF?text=Error+Loading"

def retry_on_failure(max_retries=3, delay=1):
    """Decorator to retry a function on failure"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    if attempt < max_retries - 1:
                        st.warning(f"Attempt {attempt + 1} failed, retrying in {delay}s...")
                        time.sleep(delay)
                    else:
                        st.error(f"Failed after {max_retries} attempts: {str(e)}")
                        return None
            return None
        return wrapper
    return decorator

class PosterLoader:
    """Enhanced poster loading with retry mechanism and error handling"""
    
    @staticmethod
    @retry_on_failure(max_retries=3, delay=1)
    def fetch_poster_with_retry(movie_id: int) -> Optional[str]:
        """
        Fetch movie poster with retry mechanism
        
        Args:
            movie_id (int): TMDB movie ID
            
        Returns:
            str: Poster URL or fallback image URL
        """
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        
        try:
            response = requests.get(url, timeout=PosterLoaderConfig.TIMEOUT)
            response.raise_for_status()
            
            data = response.json()
            poster_path = data.get('poster_path')
            
            if poster_path:
                full_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                return full_url
            else:
                return PosterLoaderConfig.FALLBACK_IMAGE
                
        except requests.exceptions.Timeout:
            st.warning("API request timed out")
            raise
        except requests.exceptions.ConnectionError:
            st.warning("Connection error - check your internet")
            raise
        except requests.exceptions.HTTPError as e:
            st.warning(f"HTTP error: {e.response.status_code}")
            raise
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
            raise
    
    @staticmethod
    def fetch_poster_safe(movie_id: int) -> str:
        """
        Safely fetch poster with comprehensive error handling
        
        Args:
            movie_id (int): TMDB movie ID
            
        Returns:
            str: Poster URL or fallback image URL
        """
        try:
            poster_url = PosterLoader.fetch_poster_with_retry(movie_id)
            if poster_url:
                return poster_url
        except Exception as e:
            st.warning(f"Could not load poster for movie ID {movie_id}: {str(e)}")
        
        return PosterLoaderConfig.FALLBACK_IMAGE
    
    @staticmethod
    def validate_poster_url(url: str) -> bool:
        """
        Validate if poster URL is accessible
        
        Args:
            url (str): Poster URL to validate
            
        Returns:
            bool: True if URL is accessible, False otherwise
        """
        try:
            response = requests.head(url, timeout=2)
            return response.status_code == 200
        except:
            return False

class ImageCache:
    """Simple image cache to avoid repeated API calls"""
    _cache = {}
    
    @classmethod
    def get(cls, movie_id: int) -> Optional[str]:
        """Get cached poster URL"""
        return cls._cache.get(movie_id)
    
    @classmethod
    def set(cls, movie_id: int, url: str):
        """Cache poster URL"""
        cls._cache[movie_id] = url
    
    @classmethod
    def clear(cls):
        """Clear cache"""
        cls._cache.clear()

def fetch_poster(movie_id: int) -> str:
    """
    Main function to fetch poster - uses cache and retry logic
    
    Args:
        movie_id (int): TMDB movie ID
        
    Returns:
        str: Poster URL
    """
    # Check cache first
    cached_url = ImageCache.get(movie_id)
    if cached_url:
        return cached_url
    
    # Fetch with retry logic
    poster_url = PosterLoader.fetch_poster_safe(movie_id)
    
    # Cache the result
    ImageCache.set(movie_id, poster_url)
    
    return poster_url

# Export functions and classes
__all__ = ['fetch_poster', 'PosterLoader', 'ImageCache', 'PosterLoaderConfig']
