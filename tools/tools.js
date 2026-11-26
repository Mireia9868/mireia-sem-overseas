const field = id => document.getElementById(id);
field('check').onclick = () => {
  const issues = [];
  try {
    const url = new URL(field('url').value);
    if (!['http:', 'https:'].includes(url.protocol)) throw Error();
    const params = url.searchParams;
    for (const name of ['utm_source', 'utm_medium', 'utm_campaign']) {
      if (!params.get(name)?.trim()) issues.push('Missing or empty: ' + name);
    }
    for (const name of new Set(params.keys())) {
      if (!name.toLowerCase().startsWith('utm_')) continue;
      if (name !== name.toLowerCase()) issues.push('Check capitalization: ' + name);
      if (params.getAll(name).length > 1) issues.push('Repeated: ' + name);
    }
    field('tags').textContent = issues.join('\n') || 'All three tags are present. No duplicate UTM keys found.';
  } catch { field('tags').textContent = 'Enter a full HTTP or HTTPS URL.'; }
};
field('format').onclick = () => {
  const words = field('words').value.split(/\r?\n/).map(word => word.trim()).filter(Boolean);
  const mode = field('match').value;
  field('list').value = [...new Set(words)].map(word => {
    if (mode === 'Exact') return '[' + word + ']';
    if (mode === 'Phrase') return '"' + word + '"';
    return word;
  }).join('\n');
};
field('compare').onclick = () => {
  const result = field('result');
  try {
    let actual = JSON.parse(field('payload').value);
    const expected = JSON.parse(field('expected').value);
    const path = field('path').value.trim();
    if (!path) { result.textContent = 'Enter the field path to inspect.'; return; }
    if (expected !== null && typeof expected === 'object') {
      result.textContent = 'Enter a single expected value, such as 0 or "USD".'; return;
    }
    for (const key of path.split('.')) {
      if (actual === null || typeof actual !== 'object' || !Object.hasOwn(actual, key)) {
        result.textContent = 'Path absent in this sample. Confirm the mapping for your platform.'; return;
      }
      actual = actual[key];
    }
    result.textContent = (actual === expected ? 'Match' : 'Mismatch') + ' · Captured ' + JSON.stringify(actual) + ' · Expected ' + JSON.stringify(expected);
  } catch { result.textContent = 'Check the JSON syntax in the payload and expected value. Put text values in double quotes.'; }
};
