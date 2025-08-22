from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent

def load_config():
    # load default config
    with open(ROOT / "config.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    # load local override if exists
    local_cfg = ROOT / "config.local.yaml"
    if local_cfg.exists():
        with open(local_cfg, "r") as f:
            local = yaml.safe_load(f)
        cfg.update(local)

    # resolve to absolute Paths
    cfg["data_dir"] = Path(cfg["data_dir"])

    return cfg

cfg = load_config()
DATA_DIR = cfg["data_dir"]



