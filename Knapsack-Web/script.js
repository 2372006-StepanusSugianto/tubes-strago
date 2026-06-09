document.addEventListener('DOMContentLoaded', () => {
    const itemsBody = document.getElementById('itemsBody');
    const addItemBtn = document.getElementById('addItemBtn');
    const solveBtn = document.getElementById('solveBtn');
    const resultSection = document.getElementById('resultSection');

    let itemCount = 0;

    // Helper to format currency/numbers if needed, but we keep it simple as requested
    
    function createRow() {
        itemCount++;
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><input type="text" class="item-name" placeholder="Nama Barang ${itemCount}" required></td>
            <td><input type="number" class="item-weight" placeholder="0" min="1" required></td>
            <td><input type="number" class="item-value" placeholder="0" min="1" required></td>
            <td><button class="btn btn-danger remove-btn">Hapus</button></td>
        `;
        
        tr.querySelector('.remove-btn').addEventListener('click', () => {
            tr.remove();
        });
        
        return tr;
    }

    // Add initial 3 rows
    for(let i=0; i<3; i++) {
        itemsBody.appendChild(createRow());
    }

    addItemBtn.addEventListener('click', () => {
        itemsBody.appendChild(createRow());
    });

    solveBtn.addEventListener('click', () => {
        const capacityInput = document.getElementById('capacity').value;
        const capacity = parseInt(capacityInput);

        if (isNaN(capacity) || capacity <= 0) {
            alert('Masukkan kapasitas tas yang valid!');
            return;
        }

        const rows = itemsBody.querySelectorAll('tr');
        const items = [];

        for (let row of rows) {
            const name = row.querySelector('.item-name').value.trim();
            const weight = parseInt(row.querySelector('.item-weight').value);
            const value = parseInt(row.querySelector('.item-value').value);

            if (!name || isNaN(weight) || isNaN(value)) {
                alert('Pastikan semua data barang terisi dengan benar!');
                return;
            }

            items.push({ nama: name, berat: weight, nilai: value });
        }

        if (items.length === 0) {
            alert('Masukkan minimal satu barang!');
            return;
        }

        // --- Backtracking Algorithm Variables ---
        let best_items = [];
        let best_weight = 0;
        let best_value = 0;
        let jumlah_node = 0;
        let langkah_eksplorasi = [];

        // --- Recursive Backtracking Function ---
        function knapsack_backtracking(index, total_berat, total_nilai, barang_dipilih) {
            jumlah_node++;

            // Record step
            langkah_eksplorasi.push({
                node: jumlah_node,
                index: index,
                berat: total_berat,
                nilai: total_nilai,
                barang: [...barang_dipilih]
            });

            // Pruning
            if (total_berat > capacity) {
                return;
            }

            // Base case
            if (index === items.length) {
                if (total_nilai > best_value) {
                    best_value = total_nilai;
                    best_weight = total_berat;
                    best_items = [...barang_dipilih];
                }
                return;
            }

            const barang = items[index];

            // Pilihan 1: ambil barang
            barang_dipilih.push(barang.nama);
            knapsack_backtracking(
                index + 1,
                total_berat + barang.berat,
                total_nilai + barang.nilai,
                barang_dipilih
            );

            // Backtrack
            barang_dipilih.pop();

            // Pilihan 2: tidak ambil barang
            knapsack_backtracking(
                index + 1,
                total_berat,
                total_nilai,
                barang_dipilih
            );
        }

        // --- Execution ---
        const startTime = performance.now();
        
        knapsack_backtracking(0, 0, 0, []);
        
        const endTime = performance.now();
        const waktu_eksekusi = (endTime - startTime).toFixed(4);

        // --- Update UI Results ---
        
        // Items list
        const ul = document.getElementById('selectedItemsList');
        ul.innerHTML = '';
        if (best_items.length === 0) {
            ul.innerHTML = '<li>Tidak ada barang yang terpilih (Kapasitas tidak cukup)</li>';
        } else {
            best_items.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item;
                ul.appendChild(li);
            });
        }

        // Stats
        document.getElementById('resWeight').textContent = best_weight;
        document.getElementById('resValue').textContent = best_value;
        document.getElementById('resRemaining').textContent = capacity - best_weight;
        document.getElementById('resNodes').textContent = jumlah_node;
        document.getElementById('resTime').textContent = waktu_eksekusi;

        // Exploration Steps (first 20)
        const expDiv = document.getElementById('explorationSteps');
        expDiv.innerHTML = '';
        
        const limit = Math.min(langkah_eksplorasi.length, 20);
        let stepText = '';
        for(let i=0; i<limit; i++) {
            const l = langkah_eksplorasi[i];
            stepText += `Node ${l.node}: index=${l.index}, berat=${l.berat}, nilai=${l.nilai}, barang=[${l.barang.join(', ')}]\n`;
        }
        if (langkah_eksplorasi.length > 20) {
            stepText += `... (Total ${langkah_eksplorasi.length} node)\n`;
        }
        expDiv.textContent = stepText;

        // Show result section with animation
        resultSection.classList.remove('hidden');
        resultSection.style.animation = 'none';
        resultSection.offsetHeight; /* trigger reflow */
        resultSection.style.animation = 'fadeInDown 0.8s ease';
        
        // Scroll to results
        resultSection.scrollIntoView({ behavior: 'smooth' });
    });
});
