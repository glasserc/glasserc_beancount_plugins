"""Try to automatically add payee information when given by narration.

This can be helpful when dealing with automatically parsed
transactions from a bank. It can be nicer to actually modify the
transaction data in the Beancount file, but this way we can update the
rules assigning transactions to payees without having to go back and
rewrite data.

"""

__plugins__ = ['add_payee_from_narration']

from beancount.core.data import Transaction

def add_payee_from_narration(entries, options_map, config):
    src, dest = config.split(':')
    src = src.strip()
    dest = dest.strip()
    new_entries = []
    for entry in entries:
        new_entry = entry
        if isinstance(entry, Transaction):
            should_set_payee = not entry.payee
            narration_matches = src in entry.narration
            if should_set_payee and narration_matches:
                new_entry = Transaction(
                    entry.meta, entry.date, entry.flag,
                    dest,
                    entry.narration, entry.tags, entry.links, entry.postings)

        new_entries.append(new_entry)

    errors = []
    return new_entries, errors
