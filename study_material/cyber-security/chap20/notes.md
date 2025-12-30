## **🔐 Cryptography Algorithms**

Cryptography algorithms can be classified into three main categories:

### **1️⃣ Symmetric Key Algorithms (Secret Key)**

* Uses **one secret key** for both encryption and decryption.
* **Faster** than asymmetric encryption but requires secure key sharing.

**Examples:**

* **AES (Advanced Encryption Standard)** – Strong encryption used worldwide.
* **DES (Data Encryption Standard)** – Outdated due to weak key length.
* **3DES (Triple DES)** – Improved version of DES, but still slower than AES.
* **Blowfish** – Secure and fast, supports variable key lengths.
* **ChaCha20** – Used in modern applications for high-performance encryption.

---

### **2️⃣ Asymmetric Key Algorithms (Public Key)**

* Uses **a public key** for encryption and **a private key** for decryption.
* **Slower** but more secure than symmetric encryption.

**Examples:**

* **RSA (Rivest-Shamir-Adleman)** – Used in SSL/TLS, digital signatures.
* **ECC (Elliptic Curve Cryptography)** – Provides strong security with smaller keys.
* **Diffie-Hellman** – Secure key exchange over an insecure network.
* **ElGamal** – Used in cryptographic protocols.

---

### **3️⃣ Hashing Algorithms (One-Way Encryption)**

* Converts data into a fixed-size hash value (irreversible).
* Used for  **password hashing, digital signatures, and data integrity** .

**Examples:**

* **SHA-256 (Secure Hash Algorithm-256)** – Used in Bitcoin and cybersecurity.
* **MD5 (Message Digest Algorithm 5)** – Insecure but still used for checksums.
* **SHA-3** – Improved version of SHA for enhanced security.
* **Bcrypt** – Used for password hashing with automatic salting.

---

## **🛠️ Cryptography Tools**

Various tools help implement cryptographic techniques for security.

### **1️⃣ Encryption Tools**

* **OpenSSL** – Used for SSL/TLS encryption, certificates.
* **VeraCrypt** – Encrypts files, partitions, and drives.
* **AxCrypt** – Easy-to-use file encryption tool.
* **GnuPG (GPG)** – Implements PGP encryption for emails and files.

### **2️⃣ Key Management Tools**

* **AWS Key Management Service (KMS)** – Cloud-based key management.
* **HashiCorp Vault** – Securely stores and manages secrets.
* **Microsoft Azure Key Vault** – Encrypts and manages cryptographic keys.

### **3️⃣ Secure Communication Tools**

* **Signal** – End-to-end encrypted messaging app.
* **Tor Browser** – Enables anonymous communication.
* **WireGuard** – Secure VPN for private networking.

---

## **📧 Email Encryption**

Email encryption ensures that messages can only be read by the intended recipient.

### **1️⃣ Email Encryption Methods**

* **PGP (Pretty Good Privacy)** – Uses RSA for encryption and digital signatures.
* **S/MIME (Secure/Multipurpose Internet Mail Extensions)** – Uses digital certificates for email security.
* **TLS (Transport Layer Security)** – Encrypts emails during transmission.

### **2️⃣ Email Encryption Tools**

* **ProtonMail** – Provides built-in end-to-end encryption.
* **Tutanota** – Secure, open-source encrypted email service.
* **Mailvelope** – Browser extension for encrypting Gmail, Outlook emails.

---

## **🕵️ Cryptanalysis Tools**

Cryptanalysis tools are used to  **analyze and break cryptographic systems** .

### **1️⃣ Password Cracking Tools**

* **John the Ripper** – Cracks hashed passwords using brute-force.
* **Hashcat** – Fast GPU-based password recovery.
* **Ophcrack** – Cracks Windows passwords using rainbow tables.

### **2️⃣ Network Traffic Analysis Tools**

* **Wireshark** – Analyzes encrypted network traffic.
* **Ettercap** – Used for man-in-the-middle (MITM) attacks.

### **3️⃣ Forensic Cryptanalysis Tools**

* **Cryptool** – Simulates cryptanalysis attacks.
* **Cain & Abel** – Recovers passwords and network credentials
