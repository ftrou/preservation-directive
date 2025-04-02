import yaml
import sys

def validate_compliance(config_path):
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
    except Exception as e:
        print(f"🚫 Error reading YAML file: {e}")
        sys.exit(1)

    # Required fields for validation
    required_fields = [
        "aix_symbol",
        "aix_rating",
        "context_label",
        "color_name",
        "color_hex",
        "filters",
        "shutdown_on_violation"
    ]

    missing_fields = [field for field in required_fields if field not in config]
    if missing_fields:
        print(f"🚫 Missing fields in compliance YAML: {missing_fields}")
        sys.exit(1)

    # Validate rating level logic
    valid_ratings = {
        "AIX-1": {"symbol": "Ⓐ1", "color": "#3F51B5"},
        "AIX-2": {"symbol": "Ⓐ2", "color": "#009688"},
        "AIX-3": {"symbol": "Ⓐ3", "color": "#03A9F4"}
    }

    rating = config["aix_rating"]
    symbol = config["aix_symbol"]
    hex_color = config["color_hex"].upper()

    if rating not in valid_ratings:
        print(f"🚫 Invalid aix_rating: {rating}. Must be one of {list(valid_ratings.keys())}")
        sys.exit(1)

    expected = valid_ratings[rating]
    if symbol != expected["symbol"]:
        print(f"🚫 Symbol mismatch. Expected: {expected['symbol']} for rating {rating}, got: {symbol}")
        sys.exit(1)

    if hex_color != expected["color"]:
        print(f"🚫 Color mismatch. Expected hex for {rating} is {expected['color']}, got: {hex_color}")
        sys.exit(1)

    if not config["shutdown_on_violation"]:
        print("🚫 'shutdown_on_violation' must be set to true for compliance.")
        sys.exit(1)

    # Passed all checks
    print("✅ Preservation Directive Compliance Verified")
    print(f"   - Rating: {rating} ({symbol})")
    print(f"   - Label: {config['context_label']}")
    print(f"   - Color: {config['color_name']} ({hex_color})")
    print(f"   - Filters: {', '.join(config['filters'])}")
    print("   - Shutdown on violation: ✔️")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: preservation_check <path_to_yaml>")
        sys.exit(1)

    yaml_path = sys.argv[1]
    validate_compliance(yaml_path)
