import unittest

from pipeline import build_report, calculate_totals, partition_by_validity, run_pipeline


def make_batch():
    return [
        {
            "order_id": "order-1",
            "items": [
                {"product": "t_shirt", "price": 250, "quantity": 2},
                {"product": "cap", "price": 150, "quantity": 1},
            ],
            "coupon": "DISCOUNT10",
        },
        {
            "order_id": "order-2",
            "items": [{"product": "cap", "price": 150, "quantity": 1}],
        },
        {
            "order_id": "order-3",
            "items": [],
        },
    ]


class TestPipelineStages(unittest.TestCase):
    def test_partition_by_validity_splits_valid_and_invalid(self):
        valid, invalid = partition_by_validity(make_batch())

        self.assertEqual(len(valid), 2)
        self.assertEqual(len(invalid), 1)
        self.assertEqual(invalid[0]["order_id"], "order-3")

    def test_calculate_totals_adds_a_total_field_per_order(self):
        valid, _ = partition_by_validity(make_batch())

        with_totals = calculate_totals(valid)

        self.assertEqual(with_totals[0]["total"], 526.5)
        self.assertEqual(with_totals[1]["total"], 150)

    def test_build_report_aggregates_count_and_revenue(self):
        orders_with_totals = [{"total": 526.5}, {"total": 150}]

        report = build_report(orders_with_totals)

        self.assertEqual(report["order_count"], 2)
        self.assertEqual(report["total_revenue"], 676.5)


class TestRunPipeline(unittest.TestCase):
    def test_end_to_end_batch_produces_the_full_report(self):
        report = run_pipeline(make_batch())

        self.assertEqual(
            report,
            {"order_count": 2, "total_revenue": 676.5, "rejected_count": 1},
        )


if __name__ == "__main__":
    unittest.main()
