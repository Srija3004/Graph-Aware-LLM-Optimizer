"""
Mistral AI client for graph-aware analysis.
"""
import json
from typing import Dict, Optional
from config import settings
import logging

logger = logging.getLogger(__name__)


class MistralClient:
    """Client for interacting with Mistral AI API."""
    
    def __init__(self):
        """Initialize Mistral client."""
        self.api_key = settings.mistral_api_key
        self.model = settings.mistral_model
        print("API KEY:", repr(self.api_key))
        print("MODEL:", self.model)
        self.client = None
        
        # Only initialize if API key is provided
        if self.api_key and self.api_key != "":
            try:
                from mistralai.client import MistralClient as MC
                self.client = MC(api_key=self.api_key)
            except ImportError:
                logger.warning("Mistral AI package not properly installed")
            except Exception as e:
                print("MISTRAL ERROR:", e)
                logger.warning(f"Failed to initialize Mistral client: {e}")
    
    def is_available(self) -> bool:
        """Check if Mistral client is available."""
        return self.client is not None
    
    async def analyze_graph_solution(self, prompt: str) -> Optional[Dict[str, str]]:
        """
        Analyze graph solution using Mistral AI.
        
        Args:
            prompt: Analysis prompt
            
        Returns:
            Dictionary with explanation, quality_assessment, and suggestions
        """
        if not self.is_available():
            return self._get_fallback_analysis()
        
        try:
            from mistralai.models.chat_completion import ChatMessage
            
            messages = [
                ChatMessage(role="user", content=prompt)
            ]
            
            # Make API call
            response = self.client.chat(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            # Extract response
            content = response.choices[0].message.content
            
            # Clean up content (remove markdown code blocks if present)
            if "```json" in content:
                content = content.replace("```json", "").replace("```", "")
            elif "```" in content:
                content = content.replace("```", "")
            
            content = content.strip()
            
            # Try to parse JSON response
            try:
                analysis = json.loads(content)
                return {
                    "explanation": self._clean_field(analysis.get("explanation", "")),
                    "quality_assessment": self._clean_field(analysis.get("quality_assessment", "")),
                    "suggestions": self._clean_field(analysis.get("suggestions", ""))
                }
            except json.JSONDecodeError:
                # If not JSON, create structured response from text
                return self._parse_text_response(content)
                
        except Exception as e:
            logger.error(f"Mistral API error: {e}")
            return self._get_fallback_analysis()
    
    def _clean_field(self, value) -> str:
        """Ensure field is a string, joining list/dict if necessary."""
        if isinstance(value, str):
            return value
        if isinstance(value, list):
            return " ".join(str(v) for v in value)
        if isinstance(value, dict):
            # Flatten dict to "key: value" pairs
            return " ".join(f"{k}: {v}" for k, v in value.items())
        return str(value)
    
    def _parse_text_response(self, text: str) -> Dict[str, str]:
        """Parse non-JSON text response into structured format."""
        lines = text.split('\n')
        return {
            "explanation": text[:200] if len(text) > 200 else text,
            "quality_assessment": "Analysis completed successfully.",
            "suggestions": "Consider experimenting with different algorithms for comparison."
        }
    
    def _get_fallback_analysis(self) -> Dict[str, str]:
        """Return fallback analysis when Mistral is not available."""
        return {
            "explanation": "Solution computed using classical graph algorithms. Mistral AI analysis is currently unavailable (API key not configured).",
            "quality_assessment": "The algorithm provides proven approximation guarantees for this NP-hard problem.",
            "suggestions": "To enable AI-powered analysis, configure your Mistral API key in the .env file."
        }


# Global Mistral client instance
mistral_client = MistralClient()
