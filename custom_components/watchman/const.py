DOMAIN = "watchman"

DEFAULT_REPORT_FILENAME = "thewatchman_report.txt"
DEFAULT_HEADER = "-== WATCHMAN REPORT ==- "

CONF_IGNORED_FILES = "ignored_files"
CONF_HEADER = "report_header"
CONF_REPORT_PATH = "report_path"
CONF_IGNORED_ITEMS = "ignored_items"
CONF_SERVICE_NAME = "service"
CONF_SERVICE_DATA = "data"
CONF_INCLUDED_FOLDERS = "included_folders"
CONF_CHECK_LOVELACE = "check_lovelace"
CONF_IGNORED_STATES = "ignored_states"
CONF_CHUNK_SIZE = "chunk_size"
CONF_CREATE_FILE = "create_file"
CONF_SEND_NITIFICATION = "send_notification"
CONF_PARSE_CONFIG = "parse_config"
CONF_COLUMNS_WIDTH = "columns_width"
CONF_STARTUP_DELAY = "startup_delay"
CONF_FRIENDLY_NAMES = "friendly_names"

EVENT_AUTOMATION_RELOADED = "automation_reloaded"
EVENT_SCENE_RELOADED = "scene_reloaded"

SENSOR_LAST_UPDATE = "sensor.watchman_last_updated"
SENSOR_MISSING_ENTITIES = "sensor.watchman_missing_entities"
SENSOR_MISSING_SERVICES = "sensor.watchman_missing_services"

TRACKED_EVENT_DOMAINS = [
    "homeassistant",
    "input_boolean",
    "input_button",
    "input_select",
    "input_number",
    "input_datetime",
    "person",
    "input_text",
    "script",
    "timer",
    "zone",
]

BUNDLED_IGNORED_ITEMS = [
    "timer.cancelled",
    "timer.finished",
    "timer.started",
    "timer.restarted",
    "timer.paused",
]