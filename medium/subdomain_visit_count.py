"""
https://leetcode.com/problems/subdomain-visit-count/

Input: Array
  - each element is count-paired domains (9001 discuss.leetcode.com)
Output: Array
  - output all count-paired domains of each subdomain in the input
  - discuss.leetcode.com -> discuss.leetcode.com, leetcode.com, .com


Example:

Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
Explanation: We only have one website domain: "discuss.leetcode.com".
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.


To me - it seems like the best data structure is a dictionary - more specifically a counter

Let's say we get this:

"9001 discuss.leetcode.com"

Put 9001 into key: discuss.leetcode.com


Overall Algorithm:
- Loop through `cpdomains`
- Create a counter called `results`
- For each cpdomain:
  - Extract the count
  - Extract the domain
  - *Using the domain, generate the subdomains that are possible*
  - Add the count to `results` using the generated subdomains as the key
- Create a dictionary called `output`
- For each domain in results
  - Create the count-paired domains and append to `output`
- Return `output`

Generate subdomains algo:
- Split the domain by "." and save it in a variable called `subdomains`
- Create an array called `results`
- For each element in `subdomains`:
  - slice idx to end of array and join with "."
  - append that to `results`
- Return `results`
"""
from typing import List
from collections import Counter


class Solution:
  def generate_subdomains(self, domain: str):
    subdomains = domain.split(".")
    results = []
    for idx in range(len(subdomains)):
      results.append(".".join(subdomains[idx:len(subdomains)]))
    return results

  def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    results = Counter()
    for domain in cpdomains:
      cnt_paired = domain.split(" ")
      visit = int(cnt_paired[0])
      subdomains = self.generate_subdomains(cnt_paired[1])
      for subdomain in subdomains:
        results[subdomain] += visit

    output = []
    for domain in results:
      subdomain_cnt_paired = f"{results[domain]} {domain}"
      output.append(subdomain_cnt_paired)

    return output
