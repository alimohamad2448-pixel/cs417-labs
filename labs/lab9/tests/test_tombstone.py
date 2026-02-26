"""
Lab 9: Tombstone Tests — YOU WRITE THESE.

Each test function has a description of what to test.
Your job is to write the implementation. Use the tests in
test_hash_table.py as examples for how to write assertions.

Run your tests:
    pytest -v -k "TestTombstones"
"""

from hash_table_open import HashTableOpen


def find_keys_for_same_slot(ht, want=3):
    buckets = {} 

    i = 0
    while True:
        k = f"k{i}"          
        slot = ht._hash(k)
        buckets.setdefault(slot, []).append(k)

        if len(buckets[slot]) >= want:
            keys = buckets[slot][:want]
            return keys, slot

        i += 1





class TestTombstones:
    """Tests that tombstones keep the hash table working correctly."""

    def test_probe_chain_survives_deletion(self):

        ht = HashTableOpen(size=3)
        

        keys, _ = find_keys_for_same_slot(ht, want=3)
        k1, k2, k3 = keys

        ht.put(k1, 1)
        ht.put(k2, 2)
        ht.put(k3, 3)

        ht.delete(k2)

   
        assert ht.get(k3) == 3

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

        keys, start_slot = find_keys_for_same_slot(ht, want=3)
        k1, k2, k3 = keys

        ht.put(k1, 1)
        ht.put(k2, 2)
        ht.put(k3, 3)

        ht.delete(k2)

    
        new_key = "new_key"
        while ht._HashTableOpen__hash(new_key) != start_slot:
            new_key += "x"

        ht.put(new_key, 999)

        assert ht.get(new_key) == 999
        assert new_key in ht
        assert len(ht) == 3


        """
        Insert a key, then delete it (creating a tombstone).
        Insert a NEW key that would land on that same slot.
        Verify the new key is stored and the count is correct.

        This tests that put() treats tombstones as open slots
        for new insertions.            """
        # TODO: write this test

    def test_count_correct_through_delete_and_reinsert(self):

        ht = HashTableOpen(size=5)

        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)
        assert len(ht) == 3

        ht.delete("b")
        assert len(ht) == 2

        ht.put("b", 22)  
        assert len(ht) == 3           
        
        ht.delete("a")
        ht.delete("c")
        assert len(ht) == 1
        assert ht.get("b") == 22
        

        """
        Start with a table, insert 3 keys (count should be 3).
        Delete one (count should be 2).
        Reinsert a key with the same name (count should be 3).
        Delete two keys (count should be 1).

        Verify len() is correct after every step.
        """
         # TODO: write this test