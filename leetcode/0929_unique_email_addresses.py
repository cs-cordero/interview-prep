from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_emails = set()
        for email in emails:
            local, domain = email.split("@")
            local, *_ = local.split("+")
            local = local.replace(".", "")
            final_emails.add(f"{local}@{domain}")
        return len(final_emails)
