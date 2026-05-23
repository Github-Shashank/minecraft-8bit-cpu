# Minecraft 8-bit CPU

A custom educational 8-bit CPU architecture built in Minecraft using Redstone.

This project includes:
- custom ISA design
- ALU architecture
- instruction decoder
- memory subsystem
- control flow system
- CALL / RET stack logic
- Django-based assembler and visual simulator

---

# Features

## ISA Architecture

The CPU uses a modular instruction architecture:

- `INS` → control flow instructions
- `DM` → data manipulation instructions
- `MEM VALUE` → embedded values/immediates

---

# Current Components

- Instruction Decoder
- Data Memory
- ALU
- Register Routing
- CMP Logic
- Jump Register
- CALL / RET System
- Stack Concept
- Web UI Simulator

---

# ALU Operations

Supported operations:

- ADD
- SUB
- NAND
- AND
- NOR
- OR
- XNOR
- XOR
- NOT
- INC
- DEC
- RS
- LS
- ROR
- ROL

---

# Control Flow

Supported control instructions:

- JMP ONLY
- JMP IF
- JMP IF NOT
- CALL
- RET

---

# Architecture Philosophy

This CPU focuses on:
- educational simplicity
- explicit datapath control
- modular hardware design
- Minecraft-friendly implementation
- visual debugging

The architecture is intentionally minimalistic and centered around:
- explicit routing
- W/Center datapath
- modular decode stages

---

# Web Interface

The project also includes a Django-based interface for:
- assembly editing
- binary compilation
- CPU visualization
- memory visualization
- ALU visualization

---

# Technologies Used

- Minecraft Redstone
- Python
- Django
- HTML/CSS/JavaScript

---

# Future Goals

- automatic instruction fetch
- complete execution cycle
- interactive step debugger
- visual datapath animation
- online assembler
- programmable ROM support

---

# License

MIT License