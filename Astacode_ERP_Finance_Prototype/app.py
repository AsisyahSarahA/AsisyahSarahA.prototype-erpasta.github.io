from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock Database
projects = [
    {"id": 1, "name": "Aplikasi Kasir RS Medika", "value": 30000000},
    {"id": 2, "name": "Web Company Profile X", "value": 15000000},
    {"id": 3, "name": "Sistem HRIS Terintegrasi", "value": 80000000},
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/invoices')
def invoices():
    return render_template('invoices.html', projects=projects)

@app.route('/expenses')
def expenses():
    return render_template('expenses.html', projects=projects)

@app.route('/reconciliation')
def reconciliation():
    return render_template('reconciliation.html')

# Placeholder routes (sidebar items)
@app.route('/payroll')
def payroll():
    return render_template('placeholder.html', title="Penggajian (Payroll)", icon="fas fa-users",
                           desc="Pengelolaan gaji tetap bulanan karyawan (OPEX). Tidak memotong margin proyek tertentu.")

@app.route('/vendor')
def vendor():
    return render_template('vendor.html', projects=projects)

@app.route('/freelancer')
def freelancer():
    return render_template('freelancer.html', projects=projects)

@app.route('/accounts')
def accounts():
    return render_template('placeholder.html', title="Daftar Rekening & Saldo", icon="fas fa-piggy-bank",
                           desc="Pemantauan semua rekening bank perusahaan (BCA, Mandiri, Kas Kecil, Valas) secara real-time.")

@app.route('/internal-transfer')
def internal_transfer():
    return render_template('placeholder.html', title="Mutasi Internal (Pindah Dana)", icon="fas fa-exchange-alt",
                           desc="Pencatatan perpindahan dana antar rekening perusahaan. Tidak mempengaruhi laporan laba/rugi.")

@app.route('/coa')
def coa():
    return render_template('placeholder.html', title="Chart of Accounts (COA)", icon="fas fa-list-ol",
                           desc="Daftar sandi kode akun standar perusahaan sebagai acuan pencatatan jurnal ganda.")

@app.route('/journal')
def journal():
    return render_template('placeholder.html', title="Jurnal Umum", icon="fas fa-book",
                           desc="Riwayat seluruh entri jurnal debit/kredit yang otomatis ter-generate dari setiap transaksi.")

@app.route('/report-company')
def report_company():
    return render_template('placeholder.html', title="Laba Rugi Perusahaan (Consolidated)", icon="fas fa-building",
                           desc="Laporan performa keuangan konsolidasi seluruh pendapatan dan pengeluaran perusahaan.")

@app.route('/report-project')
def report_project():
    return render_template('placeholder.html', title="Profitabilitas Proyek (P&L per Project)", icon="fas fa-project-diagram",
                           desc="Kalkulasi otomatis laba bersih per proyek. Rumus: [Total Termin Lunas] - [Total HPP Proyek].")

if __name__ == '__main__':
    print("Membuka server di http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
