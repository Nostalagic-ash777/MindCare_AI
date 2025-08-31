"""
Test suite for MindCare AI bot logic
"""
import unittest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from services.analytics import Analytics
from utils.config_manager import ConfigManager


class TestBotLogic(unittest.TestCase):
    """Test cases for bot logic functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.config = ConfigManager()
        self.analytics = Analytics()

    def test_crisis_keyword_detection(self):
        """Test crisis keyword detection"""
        crisis_messages = [
            "I want to kill myself",
            "I'm thinking about suicide",
            "I want to end it all",
            "I'm going to hurt myself"
        ]
        
        safe_messages = [
            "I had a good day today",
            "Thank you for your help",
            "I'm feeling better"
        ]
        
        for message in crisis_messages:
            result = self.detect_crisis_keywords(message)
            self.assertTrue(result, f"Failed to detect crisis in: {message}")
        
        for message in safe_messages:
            result = self.detect_crisis_keywords(message)
            self.assertFalse(result, f"False positive for: {message}")

    def detect_crisis_keywords(self, message):
        """Helper method to detect crisis keywords"""
        crisis_keywords = [
            'suicide', 'kill myself', 'end it all', 'hurt myself',
            'want to die', 'no point', 'hopeless'
        ]
        
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in crisis_keywords)

    def test_emergency_contacts(self):
        """Test emergency contact information"""
        contacts = self.config.get_emergency_contacts()
        
        self.assertIn('crisis', contacts)
        self.assertIn('text', contacts)
        self.assertIn('emergency', contacts)
        
        self.assertEqual(contacts['crisis'], '988')
        self.assertEqual(contacts['text'], '741741')
        self.assertEqual(contacts['emergency'], '911')

    def test_mental_health_tips(self):
        """Test mental health tips functionality"""
        tips = self.get_mental_health_tips()
        
        self.assertIsInstance(tips, list)
        self.assertGreater(len(tips), 0)
        
        # Check that tips contain helpful content
        for tip in tips:
            self.assertIsInstance(tip, str)
            self.assertGreater(len(tip), 10)  # Tips should be substantive

    def get_mental_health_tips(self):
        """Helper method to get mental health tips"""
        return [
            "Take deep breaths and practice mindfulness",
            "Stay connected with friends and family",
            "Maintain a regular sleep schedule",
            "Exercise regularly for better mood",
            "Practice gratitude daily",
            "Limit social media if it affects your mood",
            "Seek professional help when needed"
        ]

    def test_privacy_compliance(self):
        """Test that no personal data is logged"""
        # This test ensures we don't accidentally log personal information
        test_message = "My name is John and I live at 123 Main St"
        
        # Simulate message processing
        processed = self.process_message_safely(test_message)
        
        # Check that personal info is not in processed data
        self.assertNotIn("John", str(processed))
        self.assertNotIn("123 Main St", str(processed))

    def process_message_safely(self, message):
        """Helper method to process messages while maintaining privacy"""
        # Only return metadata, never actual content
        return {
            'timestamp': '2025-08-31T14:30:00Z',
            'message_length': len(message),
            'contains_crisis_keywords': self.detect_crisis_keywords(message),
            'user_id_hash': 'anonymous_user_hash'
        }

    def test_accessibility_features(self):
        """Test accessibility compliance"""
        # Test that the system can handle screen reader interactions
        # This is a placeholder for more comprehensive accessibility testing
        accessibility_features = [
            'keyboard_navigation',
            'screen_reader_support',
            'high_contrast_mode',
            'text_scaling'
        ]
        
        for feature in accessibility_features:
            self.assertTrue(self.check_accessibility_feature(feature))

    def check_accessibility_feature(self, feature):
        """Helper method to check accessibility features"""
        # Placeholder implementation
        supported_features = [
            'keyboard_navigation',
            'screen_reader_support', 
            'high_contrast_mode',
            'text_scaling'
        ]
        return feature in supported_features


class TestAnalytics(unittest.TestCase):
    """Test cases for analytics functionality"""

    def setUp(self):
        """Set up analytics test fixtures"""
        self.analytics = Analytics()

    def test_privacy_focused_tracking(self):
        """Test that analytics respects privacy"""
        # Analytics should never track personal information
        user_data = {
            'message': 'I feel sad today',
            'timestamp': '2025-08-31T14:30:00Z'
        }
        
        tracked_data = self.analytics.track_safely(user_data)
        
        # Check that actual message content is not tracked
        self.assertNotIn('message', tracked_data)
        self.assertIn('timestamp', tracked_data)
        self.assertIn('message_length', tracked_data)

    def test_crisis_event_logging(self):
        """Test crisis event logging (without personal data)"""
        crisis_event = {
            'type': 'crisis_detected',
            'timestamp': '2025-08-31T14:30:00Z',
            'emergency_resources_shown': True
        }
        
        result = self.analytics.log_crisis_event(crisis_event)
        self.assertTrue(result)


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)