"""Minimal Streamlit UI."""

try:  # pragma: no cover - optional dependency
    import streamlit as st
except Exception:  # pragma: no cover
    st = None


def main() -> None:
    if st is None:
        raise RuntimeError("streamlit is required to run the UI")
    st.title("Catma UI")


if __name__ == "__main__":  # pragma: no cover
    main()
