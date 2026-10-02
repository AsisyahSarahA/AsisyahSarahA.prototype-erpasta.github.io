/**
 * Dynamic Shared Sidebar Component - ASTACODE ERP
 * Integrates index.html & crm.html with real-time active state & CRM accordion submenu
 */

(function() {
  const SIDEBAR_ICONS = {
    brand: '<path d="M12 3l2.2 6.8H21l-5.5 4 2.1 6.7L12 16.4 6.4 20.5 8.5 13 3 9.8h6.8L12 3z"/>',
    dashboard: '<path d="M4 13h6V4H4v9zm10 7h6v-9h-6v9zM4 20h6v-3H4v3zm10-10h6V4h-6v6z"/>',
    crm: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm12 10v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    pipeline: '<path d="M4 5h6v5H4V5zm10 0h6v5h-6V5zM4 14h6v5H4v-5zm10 0h6v5h-6v-5z"/>',
    briefcase: '<path d="M4 7h16v13H4zM8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M4 12h16M10 12v2h4v-2"/>',
    bug: '<path d="M20 13c0 5-3.5 8.6-6.6 9.4-1 .3-2 .3-2.8 0-3.1-.8-6.6-4.4-6.6-9.4C4 8.5 7.6 5 12 5s8 3.5 8 8z M12 5V2 M8 5L6 3 M16 5l2-2 M4 11h2 M18 11h2 M5 16l-2 2 M19 16l2 2 M9 10h6 M9 14h6"/>',
    wallet: '<path d="M20 7H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z M16 14h.01 M20 7V5a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v2"/>',
    megaphone: '<path d="M3 11v2a2 2 0 0 0 2 2h2l4 6h2l-2.5-6H19a2 2 0 0 0 2-2v-2a2 2 0 0 0-2-2H10L5 6v5z"/>',
    spark: '<path d="M12 2l3 6 6 3-6 3-3 6-3-6-6-3 6-3z"/>',
    bot: '<path d="M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V7h1a7 7 0 0 1 7 7h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-1H2a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h1a7 7 0 0 1 7-7h1V5.73c-.6-.34-1-.99-1-1.73a2 2 0 0 1 2-2zM9 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm6 0a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/>',
    chart: '<path d="M18 20V10M12 20V4M6 20v-6"/>',
    plug: '<path d="M8 12l4-4m-6 8 4-4m6-8v4m0 0h4m-4 0a5 5 0 0 1-5 5H9a5 5 0 0 0 0 10h4"/>',
    shield: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    settings: '<path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
    chevron: '<polyline points="9 18 15 12 9 6"></polyline>'
  };

  function svg(name, className = '') {
    const p = SIDEBAR_ICONS[name] || '';
    return `<svg class="${className}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${p}</svg>`;
  }

  window.renderDynamicSidebar = function(config = {}) {
    const isCrmDoc = window.location.pathname.toLowerCase().includes('crm.html');
    
    // Determine active items
    const activePage = config.activePage || (isCrmDoc ? 'crm' : 'dashboard');
    const activeSubpage = config.activeSubpage || (isCrmDoc ? 'pipeline' : '');

    const sidebarHtml = `
      <aside class="sidebar" id="sidebar">
        <!-- Brand Header -->
        <a href="index.html#dashboard" class="brand" data-nav="dashboard">
          <div class="brand-mark">
            ${svg('brand')}
          </div>
          <div>
            <h1>ASTACODE ERP</h1>
            <p>Enterprise Operations Platform</p>
          </div>
        </a>

        <!-- Workspace Nav -->
        <div class="nav-label">Workspace</div>
        <nav class="nav" id="sidebar-nav-workspace">
          <!-- Dashboard -->
          <a href="index.html#dashboard" class="nav-btn ${activePage === 'dashboard' ? 'active' : ''}" data-nav="dashboard">
            ${svg('dashboard')}
            <span>Dashboard</span>
          </a>

          <!-- CRM Module with Collapsible Submenu -->
          <div class="nav-group ${activePage === 'crm' ? 'open' : ''}" id="crmNavGroup">
            <button type="button" class="nav-btn nav-parent-btn ${activePage === 'crm' ? 'active' : ''}" id="crmParentToggle" onclick="window.toggleCrmAccordion(event)">
              <div class="nav-left">
                ${svg('crm')}
                <span>CRM Module</span>
              </div>
              ${svg('chevron', 'nav-chevron')}
            </button>
            <div class="nav-sub" id="crmSubNav">
              <a href="crm.html#pipeline" class="nav-sub-btn ${activePage === 'crm' && (activeSubpage === 'pipeline' || !activeSubpage) ? 'active' : ''}" data-crm-sub="pipeline" onclick="window.handleCrmNav('pipeline', event)">
                <span class="nav-sub-dot"></span>
                <span>Lead & Pipeline</span>
              </a>
              <a href="crm.html#quotation" class="nav-sub-btn ${activePage === 'crm' && activeSubpage === 'quotation' ? 'active' : ''}" data-crm-sub="quotation" onclick="window.handleCrmNav('quotation', event)">
                <span class="nav-sub-dot"></span>
                <span>Quotation & MoU</span>
              </a>
              <a href="crm.html#customer" class="nav-sub-btn ${activePage === 'crm' && activeSubpage === 'customer' ? 'active' : ''}" data-crm-sub="customer" onclick="window.handleCrmNav('customer', event)">
                <span class="nav-sub-dot"></span>
                <span>Master Customer</span>
              </a>
              <a href="crm.html#master" class="nav-sub-btn ${activePage === 'crm' && activeSubpage === 'master' ? 'active' : ''}" data-crm-sub="master" onclick="window.handleCrmNav('master', event)">
                <span class="nav-sub-dot"></span>
                <span>Master Data CRM</span>
              </a>
              <a href="crm.html#analytics" class="nav-sub-btn ${activePage === 'crm' && activeSubpage === 'analytics' ? 'active' : ''}" data-crm-sub="analytics" onclick="window.handleCrmNav('analytics', event)">
                <span class="nav-sub-dot"></span>
                <span>Revenue Forecast</span>
              </a>
            </div>
          </div>

          <!-- Project Management -->
          <a href="index.html#projects" class="nav-btn ${activePage === 'projects' ? 'active' : ''}" data-nav="projects">
            ${svg('briefcase')}
            <span>Project Management</span>
          </a>

          <!-- Automation Fix Bug -->
          <a href="index.html#automation" class="nav-btn ${activePage === 'automation' ? 'active' : ''}" data-nav="automation">
            ${svg('bug')}
            <span>Automation Fix Bug</span>
          </a>

          <!-- Finance & AR -->
          <a href="index.html#finance" class="nav-btn ${activePage === 'finance' ? 'active' : ''}" data-nav="finance">
            ${svg('wallet')}
            <span>Finance & AR</span>
          </a>

          <!-- Marketing Module -->
          <div class="nav-group ${activePage === 'marketing' ? 'open' : ''}" id="marketingNavGroup">
            <button type="button" class="nav-btn nav-parent-btn ${activePage === 'marketing' ? 'active' : ''}" id="marketingParentToggle" onclick="window.toggleMarketingAccordion(event)">
              <div class="nav-left">
                ${svg('megaphone')}
                <span>Marketing Module</span>
              </div>
              ${svg('chevron', 'nav-chevron')}
            </button>
            <div class="nav-sub" id="marketingSubNav">
              <a href="marketing.html#marketing-ops" class="nav-sub-btn ${activePage === 'marketing' && (activeSubpage === 'marketing-ops' || !activeSubpage) ? 'active' : ''}" data-marketing-sub="marketing-ops" onclick="window.handleMarketingNav('marketing-ops', event)">
                <span class="nav-sub-dot"></span>
                <span>Marketing Ops</span>
              </a>
              <a href="marketing.html#ai-engine" class="nav-sub-btn ${activePage === 'marketing' && activeSubpage === 'ai-engine' ? 'active' : ''}" data-marketing-sub="ai-engine" onclick="window.handleMarketingNav('ai-engine', event)">
                <span class="nav-sub-dot"></span>
                <span>AI Content Engine</span>
              </a>
              <a href="marketing.html#approval-queue" class="nav-sub-btn ${activePage === 'marketing' && activeSubpage === 'approval-queue' ? 'active' : ''}" data-marketing-sub="approval-queue" onclick="window.handleMarketingNav('approval-queue', event)">
                <span class="nav-sub-dot"></span>
                <span>Antrean Persetujuan</span>
              </a>
              <a href="marketing.html#calendar" class="nav-sub-btn ${activePage === 'marketing' && activeSubpage === 'calendar' ? 'active' : ''}" data-marketing-sub="calendar" onclick="window.handleMarketingNav('calendar', event)">
                <span class="nav-sub-dot"></span>
                <span>Content Calendar</span>
              </a>
              <a href="marketing.html#distribution" class="nav-sub-btn ${activePage === 'marketing' && activeSubpage === 'distribution' ? 'active' : ''}" data-marketing-sub="distribution" onclick="window.handleMarketingNav('distribution', event)">
                <span class="nav-sub-dot"></span>
                <span>Distribution Manager</span>
              </a>
              <a href="marketing.html#asset-library" class="nav-sub-btn ${activePage === 'marketing' && activeSubpage === 'asset-library' ? 'active' : ''}" data-marketing-sub="asset-library" onclick="window.handleMarketingNav('asset-library', event)">
                <span class="nav-sub-dot"></span>
                <span>Brand Asset Library</span>
              </a>
              <a href="marketing.html#social-listening" class="nav-sub-btn ${activePage === 'marketing' && activeSubpage === 'social-listening' ? 'active' : ''}" data-marketing-sub="social-listening" onclick="window.handleMarketingNav('social-listening', event)">
                <span class="nav-sub-dot"></span>
                <span>Social Listening</span>
              </a>
              <a href="marketing.html#inbox" class="nav-sub-btn ${activePage === 'marketing' && activeSubpage === 'inbox' ? 'active' : ''}" data-marketing-sub="inbox" onclick="window.handleMarketingNav('inbox', event)">
                <span class="nav-sub-dot"></span>
                <span>Omnichannel Inbox</span>
              </a>
              <a href="marketing.html#content-history" class="nav-sub-btn ${activePage === 'marketing' && activeSubpage === 'content-history' ? 'active' : ''}" data-marketing-sub="content-history" onclick="window.handleMarketingNav('content-history', event)">
                <span class="nav-sub-dot"></span>
                <span>Riwayat Konten</span>
              </a>
            </div>
          </div>

          <!-- Kanban AI Global -->
          <a href="index.html#aikanban" class="nav-btn ${activePage === 'aikanban' ? 'active' : ''}" data-nav="aikanban">
            ${svg('bot')}
            <span>Kanban AI (Global)</span>
          </a>
        </nav>

        <!-- Control & Config Nav -->
        <div class="nav-label">Control & Config</div>
        <nav class="nav" id="sidebar-nav-config">
          <a href="index.html#analytics" class="nav-btn ${activePage === 'analytics' ? 'active' : ''}" data-nav="analytics">
            ${svg('chart')}
            <span>Reporting</span>
          </a>
          <a href="index.html#integrations" class="nav-btn ${activePage === 'integrations' ? 'active' : ''}" data-nav="integrations">
            ${svg('plug')}
            <span>Integrations</span>
          </a>
          <a href="index.html#rbac" class="nav-btn ${activePage === 'rbac' ? 'active' : ''}" data-nav="rbac">
            ${svg('shield')}
            <span>Access & Audit</span>
          </a>
          <a href="index.html#settings" class="nav-btn ${activePage === 'settings' ? 'active' : ''}" data-nav="settings">
            ${svg('settings')}
            <span>Settings</span>
          </a>
        </nav>

        <!-- Sidebar User Profile Footer -->
        <div class="sidebar-bottom">
          <div class="mini-user">
            <div class="avatar">AS</div>
            <div>
              <strong>Asisyah Sarah A.</strong>
              <span>Project Manager</span>
            </div>
          </div>
        </div>
      </aside>
    `;

    // Target mount container
    let container = document.getElementById('sidebar-container');
    if (!container) {
      const existingSidebar = document.getElementById('sidebar');
      if (existingSidebar) {
        existingSidebar.outerHTML = sidebarHtml;
        setupListeners();
        return;
      }
      const app = document.querySelector('.app') || document.body;
      container = document.createElement('div');
      container.id = 'sidebar-container';
      app.insertBefore(container, app.firstChild);
    }
    container.innerHTML = sidebarHtml;
    setupListeners();
  };

  // Toggle CRM Accordion Submenu
  window.toggleCrmAccordion = function(e) {
    if (e) e.preventDefault();
    const group = document.getElementById('crmNavGroup');
    if (!group) return;
    group.classList.toggle('open');
  };

  // Handle CRM Sub Navigation
  window.handleCrmNav = function(subpage, e) {
    const isCrmDoc = window.location.pathname.toLowerCase().includes('crm.html');
    if (isCrmDoc) {
      if (e) e.preventDefault();
      if (typeof window.switchCrmPage === 'function') {
        window.switchCrmPage(subpage);
      }
      // Update active sub-btn
      document.querySelectorAll('#crmSubNav .nav-sub-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.crmSub === subpage);
      });
      // Close mobile sidebar if open
      const sb = document.getElementById('sidebar');
      if (sb) sb.classList.remove('open');
    }
    // If in index.html, user clicked link href="crm.html#<subpage>", let browser smoothly navigate!
  };

  // Toggle Marketing Accordion Submenu
  window.toggleMarketingAccordion = function(e) {
    if (e) e.preventDefault();
    const group = document.getElementById('marketingNavGroup');
    if (!group) return;
    group.classList.toggle('open');
  };

  // Handle Marketing Sub Navigation
  window.handleMarketingNav = function(subpage, e) {
    const isMarketingDoc = window.location.pathname.toLowerCase().includes('marketing.html');
    if (isMarketingDoc) {
      if (e) e.preventDefault();
      if (typeof window.switchMarketingPage === 'function') {
        window.switchMarketingPage(subpage);
      }
      // Update active sub-btn
      document.querySelectorAll('#marketingSubNav .nav-sub-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.marketingSub === subpage);
      });
      // Close mobile sidebar if open
      const sb = document.getElementById('sidebar');
      if (sb) sb.classList.remove('open');
    }
  };

  // Setup event listeners for in-page navigation (like index.html single page router)
  function setupListeners() {
    const menuBtn = document.getElementById('mobileMenu');
    if (menuBtn) {
      menuBtn.onclick = function() {
        const sb = document.getElementById('sidebar');
        if (sb) sb.classList.toggle('open');
      };
    }

    // In-page navigation handler for index.html
    const isIndexDoc = !window.location.pathname.toLowerCase().includes('crm.html');
    if (isIndexDoc) {
      document.querySelectorAll('#sidebar [data-nav]').forEach(el => {
        el.addEventListener('click', function(e) {
          const page = this.getAttribute('data-nav');
          if (typeof window.showPage === 'function') {
            e.preventDefault();
            window.showPage(page);

            // Update active states
            document.querySelectorAll('#sidebar .nav-btn').forEach(b => {
              if (!b.classList.contains('nav-parent-btn')) {
                b.classList.toggle('active', b.getAttribute('data-nav') === page);
              }
            });

            // Close mobile drawer
            const sb = document.getElementById('sidebar');
            if (sb) sb.classList.remove('open');
          }
        });
      });
    }
  }

  // Auto initialize on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('sidebar-container') || document.getElementById('sidebar');
    if (container) {
      const activePage = container.getAttribute('data-active-page');
      const activeSubpage = container.getAttribute('data-active-subpage');
      window.renderDynamicSidebar({ activePage, activeSubpage });
    }
  });
})();
