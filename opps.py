import streamlit as st

# OOP Class for Voting System
class VotingSystem:
    
    def __init__(self):
        self.candidates = ["Candidate A", "Candidate B", "Candidate C"]
        self.votes = {candidate: 0 for candidate in self.candidates}
        self.voted_users = set()

    # Method to cast vote
    def cast_vote(self, user, candidate):
        if user in self.voted_users:
            return "already_voted"
        
        if candidate in self.votes:
            self.votes[candidate] += 1
            self.voted_users.add(user)
            return "success"

    # Method to get results
    def get_results(self):
        return self.votes

    # Method to find winner
    def get_winner(self):
        return max(self.votes, key=self.votes.get)


# Store object in session state
if "system" not in st.session_state:
    st.session_state.system = VotingSystem()

system = st.session_state.system

# Streamlit UI
st.title("🗳️ Voting Management System")

st.write("Simple Online Voting System using Python and Streamlit")

# User login
user = st.text_input("Enter your Voter ID")

candidate = st.selectbox(
    "Select Candidate",
    system.candidates
)

# Vote button
if st.button("Submit Vote"):
    result = system.cast_vote(user, candidate)

    if result == "already_voted":
        st.error("⚠️ You have already voted!")
    else:
        st.success("✅ Vote submitted successfully!")

# Show results
st.subheader("📊 Voting Results")

results = system.get_results()

for candidate, vote in results.items():
    st.write(f"{candidate} : {vote} votes")

# Winner
if st.button("Show Winner"):
    winner = system.get_winner()
    st.success(f"🏆 Winner is {winner}")