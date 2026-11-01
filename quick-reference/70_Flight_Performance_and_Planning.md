# Flight Performance and Planning — Quick Reference

*Use the aircraft's approved charts and current fuel rules; memory formulas do not replace them.*

## Mass and balance

\[
\text{Moment}=\text{mass}\times\text{arm}
\qquad
\text{CG}=\frac{\sum\text{moments}}{\sum\text{mass}}
\]

```text
List loads → calculate moments → total mass/moment → CG → check envelope
```

- Secure loads to prevent movement; include the correct fuel, occupants, and equipment.
- Stay within mass limits and the approved CG envelope for take-off and landing.
- Avgas 100LL density in the bank: approximately **0.72 kg/L** (use the value specified by the problem/POH).

## Time, fuel, wind

\[
\text{Time(min)}=\frac{\text{Distance(NM)}\times60}{GS(kt)}
\qquad
\text{Fuel}=\text{flow}\times\text{time}
\]

For wind angle \(\theta\) from track (rough component estimate):
\[
\text{Headwind}=W\cos\theta,\qquad \text{Crosswind}=W\sin\theta
\]

- Headwind reduces groundspeed; tailwind increases it.
- Fuel plan: taxi + trip + required contingency/reserve/alternate fuel for the applicable operation.
- Density altitude rises with high temperature, high elevation, and low pressure → performance generally decreases.

## Performance charts

- Use the stated mass, pressure altitude, temperature, wind, runway surface/slope, and configuration.
- Tailwind, uphill slope, increased mass, and poor surface generally increase distance; verify exact corrections in POH/AFM.
- Climb gradient (height/distance) is not the same as rate of climb (height/time).
- Recompute ETA/fuel from actual groundspeed and remaining route; keep units and UTC explicit.
