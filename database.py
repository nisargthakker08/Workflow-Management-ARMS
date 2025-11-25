# database.py - Supabase Database Integration
import os
from supabase import create_client, Client
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

class SupabaseDB:
    """Supabase database connection and operations"""
    # database.py - Supabase Database Integrationimport osfrom supabase import create_client, Clientfrom typing import Optional, List, Dict, Anyfrom datetime import datetime, timedeltaimport pandas as pdimport streamlit as st
class SupabaseDB:"""Supabase database connection and operations"""def __init__(self):# Try to get credentials from Streamlit secrets first, then environmenttry:# Corrected credentials - remove the actual URLs/keys from code            self.url = st.secrets["SUPABASE_URL"]            self.key = st.secrets["SUPABASE_KEY"]except:            self.url = os.getenv("SUPABASE_URL")            self.key = os.getenv("SUPABASE_KEY")if not self.url or not self.key:            st.error("Missing Supabase credentials. Please check your configuration.")raise ValueError("Missing Supabase credentials")try:            self.client: Client = create_client(self.url, self.key)            st.success("✅ Database connected successfully!")except Exception as e:            st.error(f"❌ Database connection failed: {str(e)}")raisedef get_tasks(self, filters: Dict = None) -> List[Dict]:"""Get tasks from database with optional filters"""try:            query = self.client.table('tasks').select('*')# Apply filters if providedif filters:for key, value in filters.items():if value:  # Only apply filter if value is not empty                        query = query.eq(key, value)                        response = query.execute()return response.data
        except Exception as e:            st.error(f"Error fetching tasks: {str(e)}")return []def create_task(self, task_data: Dict) -> Dict:"""Create a new task in database"""try:            response = self.client.table('tasks').insert(task_data).execute()if response.data:return response.data[0]return Noneexcept Exception as e:            st.error(f"Error creating task: {str(e)}")return Nonedef update_task(self, task_id: int, updates: Dict) -> bool:"""Update a task in database"""try:            response = self.client.table('tasks').update(updates).eq('Task_ID', task_id).execute()return len(response.data) > 0except Exception as e:            st.error(f"Error updating task: {str(e)}")return Falsedef get_analyst_performance(self) -> List[Dict]:"""Get analyst performance data"""try:# This would be a more complex query in real implementation            response = self.client.table('tasks').select('*').execute()return response.data
        except Exception as e:            st.error(f"Error fetching performance data: {str(e)}")return []def sign_in(self, email: str, password: str) -> Dict[str, Any]:"""Sign in user - you might want to use Supabase Auth"""try:            response = self.client.auth.sign_in_with_password({"email": email,"password": password
            })return {"success": True, "user": response.user, "session": response.session}except Exception as e:return {"success": False, "error": str(e)}# Global instance
db = Nonetry:
    db = SupabaseDB()except Exception as e:
    st.warning(f"Database not available: {str(e)}. Using local storage.")

    def __init__(self):
        # Try to get credentials from Streamlit secrets first, then environment
        try:
            self.url = st.secrets.get("https://dkeypaumcjaqppqmumca.supabase.co")
            self.key = st.secrets.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRrZXlwYXVtY2phcXBwcW11bWNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjM5NzE4NTEsImV4cCI6MjA3OTU0Nzg1MX0.w3iQX7Pna4HXqZwgQqAQ5F9tLFfnSyVbHy7GfBKHuN")
            self.service_key = st.secrets.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRrZXlwYXVtY2phcXBwcW11bWNhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2Mzk3MTg1MSwiZXhwIjoyMDc5NTQ3ODUxfQ.VYJ_JhA2NHGs-qJZKnNE-Su91--6lK3kvQy6HuOrTjE")
        except:
            self.url = os.getenv("SUPABASE_URL")
            self.key = os.getenv("SUPABASE_ANON_KEY")
            self.service_key = os.getenv("SUPABASE_SERVICE_KEY")
        
        if not self.url or not self.key:
            raise ValueError("Missing Supabase credentials")
        
        self.client: Client = create_client(self.url, self.key)
    
    def sign_in(self, email: str, password: str) -> Dict[str, Any]:
        """Sign in user"""
        try:
            response = self.client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            return {"success": True, "user": response.user, "session": response.session}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_dashboard_metrics(self, user_id: Optional[str] = None) -> Dict:
        """Get dashboard metrics"""
        # Add your implementation here
        return {
            "total_tasks": 0,
            "pending_tasks": 0,
            "my_tasks": 0,
            "completed_tasks": 0
        }

# Global instance
try:
    db = SupabaseDB()
except Exception as e:
    print(f"Database initialization failed: {e}")
    db = None
