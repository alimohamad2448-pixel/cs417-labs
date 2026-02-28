"""
Lab 9: Tombstone Tests — YOU WRITE THESE.

Each test function has a description of what to test.
Your job is to write the implementation. Use the tests in
test_hash_table.py as examples for how to write assertions.

Run your tests:
    pytest -v -k "TestTombstones"
"""

from hash_table_open import HashTableOpen





class TestTombstones:
    """Tests that tombstones keep the hash table working correctly."""

    def test_probe_chain_survives_deletion(self):

        ht = HashTableOpen(size=3)
        

        ht.put(0, "a")
        ht.put(3, "b")
        ht.put(6, "c")

        ht.delete(3)  

        assert ht.get(0) == "a"
        assert ht.get(6) == "c"

        """
        Insert three keys that collide (use a small table, like size=3).
        Delete the MIDDLE one.
        Verify that you can still find the LAST one.

        This is the core tombstone test — if delete uses None instead
        of a tombstone, this test will fail because the probe chain breaks.
        """
        # TODO: write this test

    def test_tombstone_slot_reused_on_insert(self):

        ht = HashTableOpen(size=3)

        ht.put(0, "a")
        ht.put(3, "b")
        ht.put(6, "c")

        ht.delete(3)

        ht.put(9, "d")
        assert ht.get(9) == "d"


        """
        Insert a key, then delete it (creating a tombstone).
        Insert a NEW key that would land on that same slot.
        Verify the new key is stored and the count is correct.

        This tests that put() treats tombstones as open slots
        for new insertions.            """
        # TODO: write this test

    def test_count_correct_through_delete_and_reinsert(self):

        ht = HashTableOpen(size=5)

        ht.put(0, 10)
        ht.put(5, 20)   
        ht.put(10, 30)  
        assert len(ht) == 3

        ht.delete(5)
        assert len(ht) == 2

        ht.put(5, 200)  
        assert len(ht) == 3
        assert ht.get(5) == 200
        

        """
        Start with a table, insert 3 keys (count should be 3).
        Delete one (count should be 2).
        Reinsert a key with the same name (count should be 3).
        Delete two keys (count should be 1).

        Verify len() is correct after every step.
        """
         # TODO: write this test