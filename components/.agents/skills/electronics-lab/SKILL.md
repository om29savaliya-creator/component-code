---
name: electronics-lab
description: >-
  Context for the Electronics Lab Simulation game project located at
  d:\Dell\Documents\python\components. Activate this skill at the start of
  every session when the user continues work on this project to instantly
  restore full project context, architecture decisions, and next steps.
---

# Electronics Lab Simulation — Project Context

## What This Project Is
A Python backend for a **simulation game of an electronics lab**.
Goal: Teach users real-world electronics through an interactive breadboard simulator.

## File Structure (4 layers)

| File | Layer | Status |
|------|-------|--------|
| `breadboard.py` | Layer 1 — Connectivity Model | ✅ Done |
| `components.py` | Layer 2 — Component Definitions | 🔲 Next |
| `solver.py` | Layer 3 — Circuit Solver (KCL/KVL) | 🔲 Pending |
| `lab.py` | Master Interface for game engine | 🔲 Pending |

## Architecture Decisions (already agreed)

- **Breadboard stores NO voltage** — it is a pure connectivity/topology model
- Each breadboard **row is a Node** — A, B, C, D, E in a row are all the same electrical node
- Pin IDs use format `"3C"`, `"14A"` (row number + pin letter)
- `Node` class tracks which holes are physically occupied
- `PowerRail` is a separate class (already done) — a single node for the full rail strip
- Voltage at any point is **computed by the CircuitSolver**, not stored anywhere

## Layer 2 — components.py (build next)
Planned classes:
- `Component` (base): node_a, node_b, pin_a, pin_b
- `VoltageSource`: voltage, polarity
- `Resistor`: resistance in Ohms
- `LED`: forward_voltage, color
- `Capacitor`: capacitance in Farads
- `Switch`: is_closed (True/False)
- `Wire`: zero resistance connection

## Layer 3 — solver.py
Uses **Nodal Analysis (KCL)**:
- Build conductance matrix (G matrix)
- Build current vector (I vector)
- Solve: G * V = I
- Output: node voltages, branch currents, power per component

## Layer 4 — lab.py
Game-facing API:
- `place_component(pin_a, pin_b, component)`
- `remove_component(component_id)`
- `solve()` → triggers CircuitSolver
- `get_voltage(pin_id)` → computed value
- `get_current(component_id)`

## Key Electronics Rules Applied
- All pins in a row are shorted together (same node)
- Voltage at a node = result of Kirchhoff's Laws on the full circuit
- Series circuit → voltage divides; Parallel circuit → same voltage, current splits
- Two conflicting voltage sources on same node = short circuit (must be handled)

