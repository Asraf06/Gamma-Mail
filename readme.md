<div align="center">
  <h1>Gamma Mail 📧</h1>
  <h3>A Python-based email application with intelligent contact management</h3>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python version">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
    <img src="https://img.shields.io/badge/Status-Stable-brightgreen" alt="Status">
  </p>
  
  <img src="https://i.imgur.com/DFY7gNT.jpeg" alt="Gamma Mail Screenshot" width="80%">
</div>

<br>

<div align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</div>

<br>

<h2 id="features">✨ Features</h2>

<table>
  <tr>
    <td width="30%">
      <h4>📬 Smart Inbox System</h4>
      <ul>
        <li>Inbox for approved contacts</li>
        <li>Uncontact folder for new senders</li>
        <li>Email organization made simple</li>
      </ul>
    </td>
    <td width="30%">
      <h4>👥 Contact Management</h4>
      <ul>
        <li>Send contact requests</li>
        <li>Approve/Reject incoming requests</li>
        <li>Search for users easily</li>
      </ul>
    </td>
    <td width="30%">
      <h4>🛠️ Utility Features</h4>
      <ul>
        <li>Export emails to text files</li>
        <li>JSON-based database</li>
        <li>No external dependencies</li>
      </ul>
    </td>
  </tr>
</table>

<br>

<h2 id="installation">⚡ Installation</h2>

<div style="background: #f5f5f5; padding: 15px; border-radius: 5px;">
  <h4>Quick Start</h4>
  <ol>
    <li>Clone the repository:</li>
    <pre><code>git clone https://github.com/yourusername/gamma-mail.git
cd gamma-mail</code></pre>
    
    <li>Run the application:</li>
    <pre><code>python main.py</code></pre>
  </ol>
  
  <h4>Requirements</h4>
  <ul>
    <li>Python 3.8+</li>
    <li>No additional packages required</li>
  </ul>
</div>

<br>

<h2 id="usage">📖 Usage Guide</h2>

<div style="display: flex; flex-wrap: wrap; gap: 20px;">
  <div style="flex: 1; min-width: 300px; background: #f8f9fa; padding: 15px; border-radius: 5px;">
    <h4>🔐 Authentication</h4>
    <p>Register with your preferred username (automatically gets @gamma.com domain):</p>
    <pre><code>Username: myname
Password: ********</code></pre>
    <p>Your email will be: <code>myname@gamma.com</code></p>
  </div>
  
  <div style="flex: 1; min-width: 300px; background: #f8f9fa; padding: 15px; border-radius: 5px;">
    <h4>✉️ Sending Emails</h4>
    <pre><code>To: friend@gamma.com
Subject: Hello!
Message: Hi there, this is Gamma Mail!</code></pre>
    <p>Emails to non-contacts go to 🆕 Uncontact folder until approved</p>
  </div>
</div>

<br>

<h2 id="architecture">🏗️ System Architecture</h2>

<details>
<summary><b>📁 Project Structure</b></summary>

```
gamma-mail/
├── models/           # Data models and database
│   ├── user.py       # User operations
│   ├── email.py      # Email storage
│   └── contact.py    # Contact management
├── services/         # Business logic
│   ├── auth_service.py     # Auth operations
│   ├── mail_service.py     # Email logic
│   └── contact_service.py  # Contact logic
├── utils/            # Helpers
│   └── helpers.py    # UI utilities
├── main.py           # Entry point
└── README.md         # Documentation
```
</details>

<br>

<div style="display: flex; gap: 20px; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 300px;">
    <h4>📊 Data Flow</h4>
    <img src="https://via.placeholder.com/400x300?text=Data+Flow+Diagram" alt="Data Flow" width="100%">
  </div>
  <div style="flex: 1; min-width: 300px;">
    <h4>🔗 Dependencies</h4>
    <ul>
      <li>Models → JSON files</li>
      <li>Services → Models</li>
      <li>Main → Services</li>
    </ul>
  </div>
</div>

<br>

<h2 id="contributing">🤝 Contributing</h2>

<p>We welcome contributions! Please follow these steps:</p>

<div style="background: #f5f5f5; padding: 15px; border-radius: 5px;">
  <ol>
    <li>Fork the project</li>
    <li>Create your feature branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
    <li>Commit your changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
    <li>Push to the branch (<code>git push origin feature/AmazingFeature</code>)</li>
    <li>Open a Pull Request</li>
  </ol>
</div>

<br>

  <p>© 2025 Gamma Mail Project</p>
</div>

<div align="center" style="margin-top: 40px;">
  <h3>🌟 Star this project on GitHub!</h3>
  <p>If you find this project useful, please consider giving it a star ⭐</p>
</div>
