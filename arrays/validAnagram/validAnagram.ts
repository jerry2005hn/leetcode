function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const count: Record<string, number> = {};

  // Count characters in s
  for (let char of s) {
    count[char] = (count[char] || 0) + 1;
  }

  // Decrease for each char in t
  for (let char of t) {
    if (!count[char]) return false;
    count[char]--;
  }

  return true;
}
