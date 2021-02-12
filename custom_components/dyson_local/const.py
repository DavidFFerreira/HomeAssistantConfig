from libdyson import DEVICE_TYPE_360_EYE, DEVICE_TYPE_PURE_COOL_LINK_DESK, DEVICE_TYPE_PURE_COOL_LINK_TOWER

DOMAIN = "dyson_local"

CONF_SERIAL = "serial"
CONF_CREDENTIAL = "credential"
CONF_DEVICE_TYPE = "device_type"

DEVICE_TYPE_NAMES = {
    DEVICE_TYPE_360_EYE: "360 Eye™ robot vacuum",
    DEVICE_TYPE_PURE_COOL_LINK_DESK: "Pure Cool Link Desktop",
    DEVICE_TYPE_PURE_COOL_LINK_TOWER: "Pure Cool Link Tower",
}

DATA_DEVICES = "devices"
DATA_DISCOVERY = "discovery"
DATA_COORDINATORS = "coordinators"
