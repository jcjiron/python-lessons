# 9️⃣ Data/Pipeline-Driven

## The idea

Data flow defines the architecture. Instead of modeling objects that
collaborate, you model **transformations** chained together: raw data
comes in one end, passes through a series of stages (map/filter/reduce),
and comes out transformed on the other end. It's lesson 8's `pipe()`,
scaled up from one operation to a **whole batch** of records.

## The stop it adds

You stop modeling "one order" as the unit of work, and start modeling the
**flow of many orders at once** as a pipeline of stages: parse → validate
→ calculate → aggregate. Each stage transforms the whole collection; none
of them is a method on an object.

**Good for:** analytics, ML, reactive systems — anywhere you process many
records at once instead of one entity at a time.
**Risk:** harder debugging — when the final output is wrong, it's hard to
tell which stage corrupted the data, since it already passed through
several transformations by the time you see it.

## Running it

No extra install — standard library `unittest`:

```bash
cd lessons/09_pipeline
python3 -m unittest test_pipeline -v
```

## The example

A batch of **raw order dicts** flows through:

```
raw orders -> partition_by_validity -> calculate_totals -> build_report
```

- `partition_by_validity(raw_orders)` — splits the batch into valid orders
  and rejects (no items), before anything else touches them.
- `calculate_totals(orders)` — maps each order to a **new** dict carrying
  a computed `total` field (same discount rules as earlier lessons).
- `build_report(orders)` — reduces the whole batch down to one aggregate:
  order count and total revenue.
- `run_pipeline(raw_orders)` — wires the stages together with `pipe`, then
  adds the rejected count from the partition step.

## What to notice

- No `Order`, `Product`, or `OrderBuilder` anywhere — just dicts flowing
  through functions. The "unit" isn't one order, it's the batch.
- `calculate_totals` never mutates an order dict in place — it builds a
  new one (`dict(order, total=...)`) per item, same immutability habit as
  lesson 8, just applied across a whole list.
- The final report (`order_count`, `total_revenue`, `rejected_count`) is
  the *only* thing this pipeline produces — if something upstream is
  wrong, you have to go stage by stage to find where, since the report
  itself won't tell you.
