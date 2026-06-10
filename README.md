# GSM 7-Bit PDU Encoder and Decoder

An implementation of the GSM 03.38 telecommunications transmission standard used to optimize message payloads. This project demonstrates low-level bitwise manipulation and packing mechanics in Python without relying on external cryptographic libraries.

---

## Technical Overview

The standard SMS payload configuration is traditionally restricted to 140 bytes (1120 bits). By utilizing GSM 7-bit PDU encoding, the payload capacity expands efficiently, allowing up to 160 characters to fit inside that identical byte footprint. The script compresses the text string by utilizing the "extra" 8th bit of each byte to store part of the subsequent character's data.

### Septet-to-Octet Packing Mechanics
* **Bit Compression**: Standard characters drop their leading 8th bit (which is always a zero) to isolate the core 7-bit character data[cite: 1].
* **The Shifting Pattern**: Characters are progressively shifted and packed so that every 8 characters are mapped precisely into 7 standard 8-bit bytes (8 characters * 7 bits = 56 bits = 7 bytes * 8 bits)[cite: 1].
* **Character 1**: Its 7 bits are placed into the first byte, leaving the 8th (most significant) bit open to be filled by the first bit of Character 2[cite: 1].
* **Character 2**: Its remaining 6 bits occupy the second byte, leaving the 7th and 8th bits open to be filled by the first 2 bits of Character 3[cite: 1].
* **Supported Alphabet**: The system relies on the standard GSM 7-bit default alphabet, which includes standard Latin letters, digits, and specific symbols[cite: 1].

### Example Walkthrough
To encode the text string `"hello"`[cite: 1]:
1. The program looks up each individual character's 7-bit hex code (e.g., `h = 0x68`, `e = 0x65`) and converts them to binary[cite: 1].
2. The bits are packed sequentially using left and right bitwise shift operations[cite: 1].
3. The final computed hexadecimal PDU string results in `E8329BFD06`[cite: 1].

---

## File Architecture

* **`pdu.py`**: Contains the core custom implementation methods for `pdu_encode(m)` and `pdu_decode(encrypted_hex)`[cite: 1].
* **`pdu_gui.py`**: A pre-configured graphical desktop user interface used to run inputs, process conversions, and track live optimization stats[cite: 1].
* **`hash.txt`**: A validation file containing the exact hash string verification signature[cite: 1].
* **`.gitignore`**: Specifies untracked background cache paths (like `__pycache__/`) to prevent system clutter in version history.

---

## How to Run the Project

### Execution via Terminal and Graphical Interface
To run the core logic or test the encoding/decoding processes directly via the main script entry point, run:
```bash
python pdu.py 
python pdu_gui.py