import streamlit as st
from imapclient import IMAPClient

# Helper function to simulate email scanning
def scan_emails(criteria):
    """Simulates scanning emails based on user-defined criteria."""
    # Simulated data
    emails = [
        {"subject": "Promotional Offer", "date": "2023-01-15"},
        {"subject": "Team Meeting Notes", "date": "2023-02-20"},
        {"subject": "Subscription Renewal", "date": "2022-12-01"},
        {"subject": "Welcome to Our Service", "date": "2021-11-05"},
        #More can be added
    ]

    # Filter emails based on criteria
    if criteria == "older than 6 months":
        return [email for email in emails if email["date"] < "2023-06-01"]
    return emails

# Streamlit app setup
st.title("Mail Cleanup Assistant")

st.write("Manage your inbox efficiently by identifying emails to delete.")

# User input for criteria
criteria = st.selectbox("Select cleanup criteria:", ["older than 6 months", "promotional emails", ])

if st.button("Scan Emails"):
    scanned_emails = scan_emails(criteria)
    st.write("### Emails Suggested for Deletion:")
    for email in scanned_emails:
        st.write(f"- **{email['subject']}** (Date: {email['date']})")

    if not scanned_emails:
        st.success("No emails matched the selected criteria.")
