import re

file_path = 'd:/laragon/www/marketing_prototype/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CSS Pie Chart with Canvas
css_pie = '''<!-- CSS Pie Chart -->
                                <div style="width:140px; height:140px; border-radius:50%; background: conic-gradient(var(--brand-primary) 0% 45%, #e11d48 45% 75%, #10b981 75% 100%); box-shadow:0 8px 16px rgba(0,0,0,0.08); position:relative; display:flex; align-items:center; justify-content:center; transition:transform 0.3s ease; cursor:pointer;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                                    <div style="width:100px; height:100px; background:#fff; border-radius:50%; box-shadow:inset 0 4px 8px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; flex-direction:column;">
                                        <i class="fa-solid fa-chart-pie" style="color:var(--text-tertiary); font-size:20px; margin-bottom:4px;"></i>
                                    </div>
                                </div>
                                <!-- Legend -->'''

canvas_pie = '''<!-- JS Canvas Pie Chart -->
                                <div style="width:180px; height:180px; position:relative;">
                                    <canvas id="contentDistributionChart"></canvas>
                                </div>
                                <!-- Legend -->'''

content = content.replace(css_pie, canvas_pie)

# 2. Add classes to progress bars and set width to 0
# Leads
content = content.replace(
    '<div style="width:85%; height:100%; background:linear-gradient(90deg, #3b82f6, #60a5fa); border-radius:4px; transition:width 1s ease-in-out;"></div>',
    '<div class="animated-progress" data-target="85%" style="width:0%; height:100%; background:linear-gradient(90deg, #3b82f6, #60a5fa); border-radius:4px; transition:width 1.5s cubic-bezier(0.4, 0, 0.2, 1);"></div>'
)

# Traffic Growth
content = content.replace(
    '<div style="width:62%; height:100%; background:linear-gradient(90deg, #10b981, #34d399); border-radius:4px; transition:width 1s ease-in-out;"></div>',
    '<div class="animated-progress" data-target="62%" style="width:0%; height:100%; background:linear-gradient(90deg, #10b981, #34d399); border-radius:4px; transition:width 1.5s cubic-bezier(0.4, 0, 0.2, 1); transition-delay: 0.2s;"></div>'
)

# Conversion
content = content.replace(
    '<div style="width:84%; height:100%; background:linear-gradient(90deg, #f59e0b, #fbbf24); border-radius:4px; transition:width 1s ease-in-out;"></div>',
    '<div class="animated-progress" data-target="84%" style="width:0%; height:100%; background:linear-gradient(90deg, #f59e0b, #fbbf24); border-radius:4px; transition:width 1.5s cubic-bezier(0.4, 0, 0.2, 1); transition-delay: 0.4s;"></div>'
)

# 3. Add scripts
scripts = '''
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Initialize Chart.js Pie Chart
            const ctx = document.getElementById('contentDistributionChart').getContext('2d');
            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Instagram', 'TikTok', 'Blog'],
                    datasets: [{
                        data: [45, 30, 25],
                        backgroundColor: ['#3b82f6', '#e11d48', '#10b981'],
                        borderWidth: 0,
                        hoverOffset: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: '70%',
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.label + ': ' + context.parsed + '%';
                                }
                            }
                        }
                    },
                    animation: {
                        animateScale: true,
                        animateRotate: true,
                        duration: 1500
                    }
                }
            });

            // Animate Progress Bars
            setTimeout(() => {
                const progressBars = document.querySelectorAll('.animated-progress');
                progressBars.forEach(bar => {
                    const targetWidth = bar.getAttribute('data-target');
                    bar.style.width = targetWidth;
                });
            }, 300); // slight delay so the user sees them load
        });
    </script>
    <!-- Application Script -->
    <script src="app.js"></script>
'''

content = content.replace('    <!-- Application Script -->\n    <script src="app.js"></script>', scripts)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("JS Analytics injected successfully!")
