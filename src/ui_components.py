"""
UI/UX Enhancement Module for Movie Recommender System
Provides improved styling and user experience components
"""

import streamlit as st
from enum import Enum

class UITheme(Enum):
    """UI Theme enumeration"""
    LIGHT = "light"
    DARK = "dark"

class UIComponents:
    """Reusable UI components for consistent styling"""
    
    @staticmethod
    def header_with_emoji(title, emoji="🎬"):
        """Display header with emoji"""
        st.markdown(f"<h1>{emoji} {title}</h1>", unsafe_allow_html=True)
    
    @staticmethod
    def info_box(message, icon="ℹ️"):
        """Display custom info box"""
        st.markdown(f"""
        <div style="padding: 10px; border-radius: 5px; background-color: #E3F2FD; border-left: 4px solid #1976D2;">
            <strong>{icon} {message}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def success_box(message, icon="✅"):
        """Display custom success box"""
        st.markdown(f"""
        <div style="padding: 10px; border-radius: 5px; background-color: #E8F5E9; border-left: 4px solid #388E3C;">
            <strong>{icon} {message}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def error_box(message, icon="❌"):
        """Display custom error box"""
        st.markdown(f"""
        <div style="padding: 10px; border-radius: 5px; background-color: #FFEBEE; border-left: 4px solid #D32F2F;">
            <strong>{icon} {message}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def movie_card(title, poster_url, year, rating, similarity_score=None):
        """Display movie card with enhanced styling"""
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(poster_url, use_column_width=True)
        
        with col2:
            st.markdown(f"### {title}")
            st.markdown(f"**Year:** {int(year) if pd.notna(year) else 'N/A'}")
            st.markdown(f"**Rating:** {'⭐' * int(rating/2)} {rating:.1f}/10")
            
            if similarity_score:
                progress_value = similarity_score / 100
                st.progress(progress_value)
                st.caption(f"Similarity: {similarity_score:.1%}")
    
    @staticmethod
    def loading_animation(message="Loading..."):
        """Display loading animation"""
        with st.spinner(f"⏳ {message}"):
            return True
    
    @staticmethod
    def custom_css():
        """Apply custom CSS styling"""
        st.markdown("""
        <style>
        .recommendation-container {
            padding: 20px;
            border-radius: 10px;
            background-color: #f8f9fa;
            margin: 10px 0;
        }
        
        .movie-title {
            font-size: 20px;
            font-weight: bold;
            color: #1f77b4;
        }
        
        .rating-badge {
            display: inline-block;
            padding: 5px 10px;
            background-color: #ffc107;
            border-radius: 20px;
            font-weight: bold;
        }
        
        .sidebar-section {
            padding: 15px;
            background-color: #f0f2f6;
            border-radius: 8px;
            margin: 10px 0;
        }
        </style>
        """, unsafe_allow_html=True)

# Export components
__all__ = ['UIComponents', 'UITheme']
