# Mist math

Humidifier sizing arithmetic: the room names the mist, the mist names the tank, and the tank names the wick.

Live at https://ilanis-agent.github.io/mistmath/

## The three tools

- **Mist plan** - mL a day = room area x ceiling x a labeled 30 mL per cubic meter, with tabletop, console and whole-house bands.
- **Tank plan** - days between refills = tank mL / daily mL (one decimal), with every-other-day, daily and twice-a-day bands.
- **Wick plan** - wick days = floor(labeled wick hours / hours a day), with full-season, half-season and monthly-consumable bands.

## Formulas and limits

- Refill rhythm rounds to one decimal and wick days floor (round half up for the decimal), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: mL per cubic meter, wick life, tank size.
- Illustrative planning arithmetic only. Distilled water and a weekly scrub beat any capacity number: a dirty tank grows its own weather. Keep the room near a labeled 40-50%; past that, the windows and the walls pay for it.

## Development

- `engine.js` - calculation and render engine (browser global `MistMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
