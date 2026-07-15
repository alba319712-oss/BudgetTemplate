import streamlit as st
import streamlit.components.v1 as components

# 1. Set the page to wide mode and give it a cool title
st.set_page_config(
    layout="wide", 
    page_title="Spiced Budget Planner 🌶️",
    page_icon="🌶️"
)

# 2. Embed the entire HTML, CSS, and JS code into a single Python string
# Note: Backslashes in regex have been escaped (\\u) to prevent Python surrogate errors
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spiced Monthly Budget Planner 🌶️</title>
  <style>
    /* Premium Color Palette: Dark Forest Green & Soft Cream */
    :root {
      --dark-green: #1b3522;
      --medium-green: #2d4f36;
      --sage-green: #8ba88f;
      --cream-bg: #fcfaf2;
      --card-cream: #f4efdf;
      --text-dark: #2a342c;
      --text-light: #fcfaf2;
      --warning-red: #d34836;
      --warning-light: #fcece9;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body {
      background-color: var(--cream-bg);
      color: var(--text-dark);
      padding: 2rem 1.5rem;
      min-height: 100vh;
      /* Custom Spice Cursor */
      cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' style='font-size:24px'><text y='24'>🌶️</text></svg>") 8 24, auto !important;
    }

    /* Keep custom cursor active over interactive elements */
    button, input, textarea, select, a, span, label {
      cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' style='font-size:24px'><text y='24'>🌶️</text></svg>") 8 24, auto !important;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    header {
      background-color: var(--dark-green);
      color: var(--text-light);
      padding: 2rem;
      border-radius: 16px;
      margin-bottom: 2rem;
      box-shadow: 0 4px 15px rgba(27, 53, 34, 0.15);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
    }

    header h1 {
      font-size: 2rem;
      margin-bottom: 0.5rem;
    }

    header p {
      color: var(--sage-green);
      font-size: 1rem;
    }

    /* Currency Dropdown in Header */
    .header-controls {
      display: flex;
      gap: 0.8rem;
      align-items: center;
    }

    .header-select {
      background-color: var(--medium-green);
      color: var(--text-light);
      border: 1px solid var(--sage-green);
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-weight: 600;
      outline: none;
    }

    /* Live Over-Budget Alert Banner */
    .alert-banner {
      display: none;
      background-color: var(--warning-red);
      color: white;
      padding: 1.2rem;
      border-radius: 12px;
      margin-bottom: 1.5rem;
      font-weight: 600;
      text-align: center;
      box-shadow: 0 4px 10px rgba(211, 72, 54, 0.2);
    }

    /* Quick Dashboard Stats */
    .summary-bar {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
      margin-bottom: 2rem;
    }

    .summary-card {
      background-color: var(--card-cream);
      padding: 1.2rem;
      border-radius: 12px;
      border: 1px solid rgba(45, 79, 54, 0.1);
      text-align: center;
    }

    .summary-label {
      font-size: 0.85rem;
      color: var(--medium-green);
      text-transform: uppercase;
      margin-bottom: 0.3rem;
      font-weight: 600;
    }

    .summary-value {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--dark-green);
    }

    /* Two Column Grid */
    .columns-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      margin-bottom: 2rem;
    }

    @media (max-width: 800px) {
      .columns-grid {
        grid-template-columns: 1fr;
      }
    }

    .card {
      background-color: var(--card-cream);
      border: 1px solid rgba(45, 79, 54, 0.12);
      border-radius: 12px;
      padding: 1.5rem;
    }

    .card-header {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--dark-green);
      margin-bottom: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid rgba(45, 79, 54, 0.15);
      padding-bottom: 0.5rem;
    }

    /* Table styling */
    table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
    }

    th {
      text-align: left;
      font-size: 0.85rem;
      text-transform: uppercase;
      color: var(--medium-green);
      padding-bottom: 0.5rem;
      border-bottom: 1px solid rgba(45, 79, 54, 0.1);
    }

    td {
      padding: 0.75rem 0;
      border-bottom: 1px solid rgba(27, 53, 34, 0.05);
      font-size: 0.95rem;
    }

    .amount-col {
      text-align: right;
      font-weight: 600;
    }

    .sum-row {
      font-weight: bold;
      font-size: 1.05rem;
      color: var(--dark-green);
    }

    /* Interactive Inputs */
    .entry-form {
      display: grid;
      grid-template-columns: 2fr 1fr auto;
      gap: 0.5rem;
      margin-top: 1rem;
    }

    input, select, textarea {
      padding: 0.5rem;
      border-radius: 6px;
      border: 1px solid rgba(27, 53, 34, 0.2);
      background-color: #fff;
      font-size: 0.9rem;
    }

    /* Buttons */
    .btn {
      background-color: var(--dark-green);
      color: var(--text-light);
      border: none;
      border-radius: 6px;
      padding: 0.5rem 1rem;
      font-weight: 600;
      transition: background 0.2s;
    }

    .btn:hover {
      background-color: var(--medium-green);
    }

    .btn-secondary {
      background-color: transparent;
      border: 1px solid var(--dark-green);
      color: var(--dark-green);
    }

    .btn-secondary:hover {
      background-color: rgba(27, 53, 34, 0.05);
    }

    .delete-btn {
      background: none;
      border: none;
      color: var(--warning-red);
      font-size: 1.1rem;
      padding: 0 0.3rem;
    }

    /* Bottom Section */
    .bottom-grid {
      display: grid;
      grid-template-columns: 1fr 1.5fr;
      gap: 2rem;
      margin-bottom: 2rem;
    }

    @media (max-width: 800px) {
      .bottom-grid {
        grid-template-columns: 1fr;
      }
    }

    textarea {
      width: 100%;
      min-height: 150px;
      border-radius: 8px;
      padding: 0.8rem;
      font-family: inherit;
      resize: vertical;
    }

    /* Footer Utility Controls */
    footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 1.5rem;
      border-top: 1px solid rgba(27, 53, 34, 0.1);
      flex-wrap: wrap;
      gap: 1rem;
    }

    .utility-btns {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .credit {
      font-size: 0.85rem;
      color: var(--medium-green);
    }
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div>
        <h1>🌻 Spiced Budget Planner</h1>
        <p>Type items naturally—our system automatically structures your emojis!</p>
      </div>
      <div class="header-controls">
        <label for="currency-select" style="color: var(--text-light); font-size: 0.9rem;">Currency:</label>
        <select id="currency-select" class="header-select" onchange="changeCurrency()">
          <option value="£">£ (GBP)</option>
          <option value="$">$ (USD/CAD)</option>
          <option value="€">€ (EUR)</option>
          <option value="¥">¥ (JPY/CNY)</option>
        </select>
      </div>
    </header>

    <!-- Over Budget Alert Banner -->
    <div id="over-budget-alert" class="alert-banner">
      🌶️ WARNING: You are spending more than you earn! Time to adjust your expenses.
    </div>

    <!-- Live Budget Status -->
    <div class="summary-bar">
      <div class="summary-card">
        <div class="summary-label">Total Income</div>
        <div class="summary-value"><span class="curr-symbol">£</span><span id="stat-total-income">0.00</span></div>
      </div>
      <div class="summary-card">
        <div class="summary-label">Total Expenses</div>
        <div class="summary-value"><span class="curr-symbol">£</span><span id="stat-total-expenses">0.00</span></div>
      </div>
      <div class="summary-card">
        <div class="summary-label">Left to Spend</div>
        <div class="summary-value"><span class="curr-symbol">£</span><span id="stat-remaining">0.00</span></div>
      </div>
    </div>

    <div class="columns-grid">
      <!-- INCOME SECTION -->
      <div class="card">
        <div class="card-header">
          <span>🟢 Income (Monthly)</span>
        </div>
        <table>
          <thead>
            <tr>
              <th>Income Item</th>
              <th class="amount-col">Amount</th>
              <th></th>
            </tr>
          </thead>
          <tbody id="income-table-body">
            <!-- Items loaded dynamically -->
          </tbody>
          <tfoot>
            <tr class="sum-row">
              <td>SUM</td>
              <td class="amount-col"><span class="curr-symbol">£</span><span id="income-sum">0.00</span></td>
              <td></td>
            </tr>
          </tfoot>
        </table>

        <!-- Add Income Form -->
        <form onsubmit="addItem(event, 'income')" class="entry-form">
          <input type="text" id="inc-name" placeholder="Salary, Leftover, etc..." required>
          <input type="number" id="inc-amount" placeholder="0.00" step="0.01" required>
          <button type="submit" class="btn">+</button>
        </form>
      </div>

      <!-- EXPENSES SECTION -->
      <div class="card">
        <div class="card-header">
          <span>🔴 Expenses (Monthly)</span>
        </div>
        <table>
          <thead>
            <tr>
              <th>Expense Item</th>
              <th class="amount-col">Amount</th>
              <th></th>
            </tr>
          </thead>
          <tbody id="expense-table-body">
            <!-- Items loaded dynamically -->
          </tbody>
          <tfoot>
            <tr class="sum-row">
              <td>SUM</td>
              <td class="amount-col"><span class="curr-symbol">£</span><span id="expense-sum">0.00</span></td>
              <td></td>
            </tr>
          </tfoot>
        </table>

        <!-- Add Expense Form -->
        <form onsubmit="addItem(event, 'expense')" class="entry-form">
          <input type="text" id="exp-name" placeholder="Rent, Groceries, Gym, etc..." required>
          <input type="number" id="exp-amount" placeholder="0.00" step="0.01" required>
          <button type="submit" class="btn">+</button>
        </form>
      </div>
    </div>

    <!-- Planners & Scratchpad section -->
    <div class="bottom-grid">
      <!-- Calendar Tasks -->
      <div class="card">
        <div class="card-header">📅 Weekly Planner Checklists</div>
        <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 0.5rem;">
          <label style="display: flex; gap: 8px;"><input type="checkbox" id="chk1" onchange="savePlanners()"> Week 1 Budget Review</label>
          <label style="display: flex; gap: 8px;"><input type="checkbox" id="chk2" onchange="savePlanners()"> Week 2 Budget Review</label>
          <label style="display: flex; gap: 8px;"><input type="checkbox" id="chk3" onchange="savePlanners()"> Week 3 Budget Review</label>
          <label style="display: flex; gap: 8px;"><input type="checkbox" id="chk4" onchange="savePlanners()"> Week 4 Budget Review</label>
        </div>
      </div>

      <!-- Free-text Notepad -->
      <div class="card">
        <div class="card-header">📝 Free-type Notepad</div>
        <textarea id="notepad" placeholder="Type thoughts, wishlist items, or financial goals here. Everything auto-saves!" oninput="savePlanners()"></textarea>
      </div>
    </div>

    <!-- Premium Template Controls & Utilities Footer -->
    <footer>
      <div class="utility-btns">
        <button onclick="clearToBlank()" class="btn btn-secondary" style="border-color: var(--warning-red); color: var(--warning-red);">Clear All Data</button>
        <button onclick="loadDemoData()" class="btn btn-secondary">Reset to Demo Data</button>
        <button onclick="exportData()" class="btn btn-secondary">💾 Backup Data</button>
        <button onclick="document.getElementById('import-file').click()" class="btn btn-secondary">📂 Load Backup</button>
        <input type="file" id="import-file" style="display: none;" accept=".json" onchange="importData(event)">
      </div>
      <div class="credit">🌶️ Spiced Budget Studio</div>
    </footer>
  </div>

  <script>
    // CLEANED TEMPLATE DATA (Amounts default to 0.00 so users can enter their own values!)
    const defaultIncome = [
      { name: '🤑 Salary', amount: 0.00 },
      { name: '❣️ socials', amount: 0.00 },
      { name: '🍺 left over monthly', amount: 0.00 },
      { name: '🦀 Overdraft', amount: 0.00 },
      { name: '🍣 left to spend monthly', amount: 0.00 }
    ];

    const defaultExpenses = [
      { name: '🏠 Rent', amount: 0.00 },
      { name: '🌶️ Groceries', amount: 0.00 },
      { name: '💸 Bill', amount: 0.00 },
      { name: '📱 Phone', amount: 0.00 },
      { name: '🎶 Spotify', amount: 0.00 },
      { name: '💔 Overdraft', amount: 0.00 },
      { name: '💳 Credit card', amount: 0.00 },
      { name: '✍️ Fraser debt', amount: 0.00 },
      { name: '🤸 Gym', amount: 0.00 },
      { name: '🌿 Council tax', amount: 0.00 }
    ];

    let incomeItems = [];
    let expenseItems = [];
    let currentCurrency = '£';

    // The Magic auto-emoji detection engine!
    function getAutoEmoji(name) {
      const lower = name.toLowerCase().trim();
      
      // If user already typed an emoji at the start, don't add another one
      // Doubled the backslashes here (\\\\) to prevent Python surrogate compilation crash!
      const emojiRegex = /^(\\\\u00a9|\\\\u00ae|[\\\\u2000-\\\\u3300]|\\\\ud83c[\\\\ud000-\\\\udfff]|\\\\ud83d[\\\\ud000-\\\\udfff]|\\\\ud83e[\\\\ud000-\\\\udfff])/g;
      if (emojiRegex.test(name)) {
        return name;
      }

      if (lower.includes('saving') || lower.includes('save') || lower.includes('savings')) return '💰 ' + name;
      if (lower.includes('salary') || lower.includes('work') || lower.includes('job') || lower.includes('pay')) return '🤑 ' + name;
      if (lower.includes('social') || lower.includes('friend') || lower.includes('party') || lower.includes('outing') || lower.includes('club')) return '❣️ ' + name;
      if (lower.includes('leftover') || lower.includes('left over')) return '🍺 ' + name;
      if (lower.includes('left to spend') || lower.includes('spend monthly')) return '🍣 ' + name;
      
      if (lower.includes('rent') || lower.includes('house') || lower.includes('home') || lower.includes('flat')) return '🏠 ' + name;
      if (lower.includes('grocery') || lower.includes('groceries') || lower.includes('food') || lower.includes('eat') || lower.includes('supermarket') || lower.includes('shop')) return '🌶️ ' + name;
      if (lower.includes('bill') || lower.includes('utility') || lower.includes('electric') || lower.includes('water') || lower.includes('gas') || lower.includes('power')) return '💸 ' + name;
      if (lower.includes('phone') || lower.includes('mobile') || lower.includes('cellular') || lower.includes('data')) return '📱 ' + name;
      if (lower.includes('spotify') || lower.includes('music') || lower.includes('netflix') || lower.includes('sub')) return '🎶 ' + name;
      if (lower.includes('overdraft')) return '💔 ' + name;
      if (lower.includes('card') || lower.includes('visa') || lower.includes('credit')) return '💳 ' + name;
      if (lower.includes('debt') || lower.includes('fraser') || lower.includes('loan')) return '✍️ ' + name;
      if (lower.includes('gym') || lower.includes('fitness') || lower.includes('workout') || lower.includes('training') || lower.includes('sport')) return '🤸 ' + name;
      if (lower.includes('tax') || lower.includes('council') || lower.includes('government')) return '🌿 ' + name;

      // Default generic emojis if nothing else matches
      return '✨ ' + name;
    }

    // Initialize or load from local storage
    window.onload = function() {
      if (localStorage.getItem('incomeItems')) {
        incomeItems = JSON.parse(localStorage.getItem('incomeItems'));
      } else {
        incomeItems = [...defaultIncome];
      }

      if (localStorage.getItem('expenseItems')) {
        expenseItems = JSON.parse(localStorage.getItem('expenseItems'));
      } else {
        expenseItems = [...defaultExpenses];
      }

      if (localStorage.getItem('currentCurrency')) {
        currentCurrency = localStorage.getItem('currentCurrency');
        document.getElementById('currency-select').value = currentCurrency;
      }

      if (localStorage.getItem('notepad')) {
        document.getElementById('notepad').value = localStorage.getItem('notepad');
      }

      for(let i=1; i<=4; i++) {
        if (localStorage.getItem('chk' + i)) {
          document.getElementById('chk' + i).checked = localStorage.getItem('chk' + i) === 'true';
        }
      }

      renderAll();
    }

    // (Remaining rendering, forms, loadDemoData and local backup logic unchanged...)
    function renderAll() {
      const symbols = document.querySelectorAll('.curr-symbol');
      symbols.forEach(span => span.textContent = currentCurrency);

      const incomeBody = document.getElementById('income-table-body');
      incomeBody.innerHTML = '';
      let totalIncome = 0;
      incomeItems.forEach((item, index) => {
        totalIncome += item.amount;
        incomeBody.innerHTML += `
          <tr>
            <td>\${item.name}</td>
            <td class="amount-col">\${currentCurrency}\${item.amount.toFixed(2)}</td>
            <td style="text-align: right;"><button class="delete-btn" onclick="removeItem('income', \${index})">×</button></td>
          </tr>
        `;
      });
      document.getElementById('income-sum').textContent = totalIncome.toFixed(2);
      document.getElementById('stat-total-income').textContent = totalIncome.toFixed(2);

      const expenseBody = document.getElementById('expense-table-body');
      expenseBody.innerHTML = '';
      let totalExpenses = 0;
      expenseItems.forEach((item, index) => {
        totalExpenses += item.amount;
        expenseBody.innerHTML += `
          <tr>
            <td>\${item.name}</td>
            <td class="amount-col">\${currentCurrency}\${item.amount.toFixed(2)}</td>
            <td style="text-align: right;"><button class="delete-btn" onclick="removeItem('expense', \${index})">×</button></td>
          </tr>
        `;
      });
      document.getElementById('expense-sum').textContent = totalExpenses.toFixed(2);
      document.getElementById('stat-total-expenses').textContent = totalExpenses.toFixed(2);

      const remaining = totalIncome - totalExpenses;
      document.getElementById('stat-remaining').textContent = remaining.toFixed(2);

      const alertBanner = document.getElementById('over-budget-alert');
      if (totalExpenses > totalIncome) {
        alertBanner.style.display = 'block';
      } else {
        alertBanner.style.display = 'none';
      }

      localStorage.setItem('incomeItems', JSON.stringify(incomeItems));
      localStorage.setItem('expenseItems', JSON.stringify(expenseItems));
      localStorage.setItem('currentCurrency', currentCurrency);
    }

    function addItem(event, type) {
      event.preventDefault();
      if (type === 'income') {
        const rawName = document.getElementById('inc-name').value;
        const name = getAutoEmoji(rawName);
        const amount = parseFloat(document.getElementById('inc-amount').value);
        incomeItems.push({ name, amount });
        document.getElementById('inc-name').value = '';
        document.getElementById('inc-amount').value = '';
      } else {
        const rawName = document.getElementById('exp-name').value;
        const name = getAutoEmoji(rawName);
        const amount = parseFloat(document.getElementById('exp-amount').value);
        expenseItems.push({ name, amount });
        document.getElementById('exp-name').value = '';
        document.getElementById('exp-amount').value = '';
      }
      renderAll();
    }

    function removeItem(type, index) {
      if (type === 'income') {
        incomeItems.splice(index, 1);
      } else {
        expenseItems.splice(index, 1);
      }
      renderAll();
    }

    function changeCurrency() {
      currentCurrency = document.getElementById('currency-select').value;
      renderAll();
    }

    function savePlanners() {
      localStorage.setItem('notepad', document.getElementById('notepad').value);
      for(let i=1; i<=4; i++) {
        localStorage.setItem('chk' + i, document.getElementById('chk' + i).checked);
      }
    }

    function loadDemoData() {
      if (confirm('Reset to standard demo data? This will overwrite current entries.')) {
        incomeItems = [...defaultIncome];
        expenseItems = [...defaultExpenses];
        renderAll();
      }
    }

    function clearToBlank() {
      if (confirm('Are you sure you want to delete everything and start with a blank budget?')) {
        incomeItems = [];
        expenseItems = [];
        renderAll();
      }
    }

    function exportData() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify({
        incomeItems,
        expenseItems,
        currentCurrency,
        notepad: document.getElementById('notepad').value
      }));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", "my_budget_backup.json");
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    }

    function importData(event) {
      const fileReader = new FileReader();
      fileReader.onload = function(e) {
        try {
          const imported = JSON.parse(e.target.result);
          if (imported.incomeItems) incomeItems = imported.incomeItems;
          if (imported.expenseItems) expenseItems = imported.expenseItems;
          if (imported.currentCurrency) {
            currentCurrency = imported.currentCurrency;
            document.getElementById('currency-select').value = currentCurrency;
          }
          if (imported.notepad) document.getElementById('notepad').value = imported.notepad;
          renderAll();
          alert('Backup data successfully loaded!');
        } catch (err) {
          alert('Failed to load backup. Ensure it is a valid file.');
        }
      };
      fileReader.readAsText(event.target.files[0]);
    }
  </script>
</body>
</html>
"""

# 3. Render the full HTML template safely using Streamlit
components.html(html_code, height=1300, scrolling=True)
