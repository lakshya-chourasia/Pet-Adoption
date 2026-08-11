## 2024-08-11 - Add Contextual ARIA Labels to Icon-Only Buttons
**Learning:** Icon-only buttons used multiple times on a single page for different items (like "Favorite" buttons on pet cards) need contextual ARIA labels (e.g., "Like Monti", "Like Thor") rather than generic ones (e.g., "Favorite") to be properly distinct for screen reader users navigating interactively.
**Action:** When adding ARIA labels to repeating icon-only interactive elements in lists or cards, dynamically incorporate the item's name or title to provide unique, contextual screen reader descriptions.
