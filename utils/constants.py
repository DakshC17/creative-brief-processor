APP_TITLE = "Creative Brief Processor"
APP_SUBTITLE = (
    "Convert unstructured creative requests into structured production briefs."
)

TEXT_AREA_PLACEHOLDER = (
    "Example:\nWe need three LinkedIn ads for our cybersecurity campaign "
    "targeting CISOs. Focus on legacy VPN risks. First draft by Friday."
)

BUTTON_LABEL = "Process Brief"

SPINNER_TEXT = "Processing request..."

ERROR_UNABLE_TO_REACH = "\u274c Unable to reach automation workflow."
ERROR_TIMEOUT = "Request timed out. Please try again."
ERROR_UNEXPECTED_RESPONSE = "Unexpected response from AI."

DUPLICATE_WARNING = "\u26a0\ufe0f Duplicate Request Detected"

PRIORITY_HIGH = "High"
PRIORITY_MEDIUM = "Medium"
PRIORITY_LOW = "Low"

PRIORITY_COLORS: dict[str, str] = {
    PRIORITY_HIGH: "#dc3545",
    PRIORITY_MEDIUM: "#fd7e14",
    PRIORITY_LOW: "#28a745",
}

WEBHOOK_TIMEOUT_SECONDS = 30
