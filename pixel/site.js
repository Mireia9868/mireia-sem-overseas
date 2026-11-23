(() => {
  const bookmarksKey = 'mireia-reading-list';
  const saved = new Set();
  try {
    const stored = JSON.parse(localStorage.getItem(bookmarksKey) || '[]');
    if (Array.isArray(stored)) stored.forEach(slug => saved.add(slug));
  } catch {}
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const pixelStar = '<span class="pixel-star" aria-hidden="true"></span>';

  function setupLibrary() {
    const library = document.querySelector('#articles');
    const results = library.querySelector('#results');
    const cards = [...results.querySelectorAll('.post-card')].map(element => {
      const anchor = element.querySelector('h3 a');
      const topic = element.querySelector('.post-meta span').textContent;
      return {
        element, topic,
        slug: new URL(anchor.href).pathname.split('/').filter(Boolean).at(-1),
        text: element.textContent.toLowerCase(),
      };
    });
    const topicButtons = [...library.querySelectorAll('[data-topic]')];
    const search = library.querySelector('#query');
    const starred = library.querySelector('.saved-filter');
    const count = library.querySelector('#result-count');
    const more = library.querySelector('#load-more');
    const empty = document.createElement('p');
    empty.className = 'empty';
    results.append(empty);

    const pageSize = 6;
    let topic = '';
    let limit = pageSize;
    let savedOnly = false;
    function update() {
      const terms = search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
      const matches = cards.filter(card => (!topic || card.topic === topic) &&
        (!savedOnly || saved.has(card.slug)) && terms.every(term => card.text.includes(term)));
      const visible = new Set(matches.slice(0, limit));
      for (const card of cards) card.element.hidden = !visible.has(card);
      for (const button of topicButtons) button.setAttribute('aria-pressed', String(button.dataset.topic === topic));
      starred.setAttribute('aria-pressed', String(savedOnly));
      count.textContent = matches.length + (matches.length === 1 ? ' article' : ' articles');
      empty.hidden = Boolean(matches.length);
      empty.textContent = savedOnly && !saved.size ? 'Star an article to keep it here for later.' : 'No articles found. Try another search or topic.';
      more.hidden = matches.length <= limit;
      return matches;
    }
    for (const button of topicButtons) button.addEventListener('click', () => {
      topic = button.dataset.topic;
      limit = pageSize;
      update();
    });
    search.addEventListener('input', () => { limit = pageSize; update(); });
    starred.addEventListener('click', () => {
      savedOnly = !savedOnly;
      topic = search.value = '';
      limit = pageSize;
      update();
    });
    more.addEventListener('click', () => {
      const firstNew = limit;
      limit += pageSize;
      update()[firstNew]?.element.querySelector('h3 a').focus();
    });
    update();
    return guideTopic => {
      topic = guideTopic;
      search.value = '';
      savedOnly = false;
      limit = pageSize;
      update();
      library.querySelector('h2').focus({ preventScroll: true });
      library.scrollIntoView();
    };
  }

  function setupMap(browseTopic) {
    const buttons = [...document.querySelectorAll('[data-path]')];
    const panel = document.querySelector('#path-result');
    const templates = [...document.querySelectorAll('template[data-route]')];
    for (const button of buttons) button.addEventListener('click', () => {
      const route = button.dataset.path;
      const template = templates.find(item => item.dataset.route === route);
      if (!template) return;
      panel.replaceChildren(template.content.cloneNode(true));
      for (const control of buttons) {
        control.setAttribute('aria-pressed', String(route === control.dataset.path));
      }
      if (!reducedMotion.matches) panel.animate(
        [{ opacity: .35, transform: 'translateY(5px)' }, { opacity: 1, transform: 'translateY(0)' }],
        { duration: 220, easing: 'ease-out' }
      );
      if (button.classList.contains('map-pin')) {
        document.querySelector('.map-nav [data-path="' + route + '"]').focus({ preventScroll: true });
        document.querySelector('#explore').scrollIntoView();
      }
    });
    panel.addEventListener('click', event => {
      const button = event.target.closest('[data-browse-topic]');
      if (button) browseTopic(button.dataset.browseTopic);
    });
    const line = document.querySelector('.type-text');
    if (reducedMotion.matches || !line) return;
    const copy = line.dataset.copy;
    let index = 0;
    line.textContent = '';
    function tick() {
      line.textContent = copy.slice(0, ++index);
      if (index < copy.length) setTimeout(tick, 29);
      else document.querySelector('.cursor').classList.add('done');
    }
    setTimeout(tick, 160);
  }

  function setupArticle() {
    const button = document.querySelector('.article-save');
    const slug = button.dataset.postId;
    function updateBookmark() {
      const active = saved.has(slug);
      button.setAttribute('aria-pressed', String(active));
      button.innerHTML = pixelStar + (active ? 'Starred' : 'Star this article');
    }
    button.addEventListener('click', () => {
      if (saved.has(slug)) saved.delete(slug);
      else saved.add(slug);
      try { localStorage.setItem(bookmarksKey, JSON.stringify([...saved])); } catch {}
      updateBookmark();
    });
    updateBookmark();
    button.hidden = false;

    const links = [...document.querySelectorAll('#contents a')];
    const headings = links.map(link => document.getElementById(decodeURIComponent(link.hash.slice(1))));
    const bar = document.querySelector('.reading-progress span');
    function updateProgress() {
      const distance = document.documentElement.scrollHeight - innerHeight;
      bar.style.transform = 'scaleX(' + (distance > 0 ? Math.min(1, Math.max(0, scrollY / distance)) : 0) + ')';
      const current = headings.findLastIndex(heading => heading?.getBoundingClientRect().top < 95);
      links.forEach((link, index) => {
        if (current === index) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }
    addEventListener('scroll', updateProgress, { passive: true });
    addEventListener('resize', updateProgress);
    addEventListener('load', updateProgress);
    updateProgress();
  }

  function setupContact() {
    const select = document.querySelector('#message-topic');
    const draft = document.querySelector('#email-mireia');
    const email = document.querySelector('.contact-address').textContent.trim();
    function updateDraft() {
      draft.href = 'mailto:' + email + '?subject=' + encodeURIComponent(select.value + ' | Mireia SEM');
    }
    select.addEventListener('change', updateDraft);
    updateDraft();
    document.querySelector('#copy-email').addEventListener('click', async () => {
      const status = document.querySelector('#contact-status');
      try {
        await navigator.clipboard.writeText(email);
        status.textContent = 'Email address copied.';
      } catch {
        status.textContent = 'Copy this address: ' + email;
      }
    });
  }

  switch (document.body.dataset.page) {
    case 'home': setupMap(setupLibrary()); break;
    case 'article': setupArticle(); break;
    case 'contact': setupContact(); break;
  }
})();
