# Laporan Smart Contract — SupplyChainKopi

## 1. Informasi Umum

| Item | Detail |
|------|--------|
| **Nama Contract** | `SupplyChainKopi` |
| **Lisensi** | MIT |
| **Versi Solidity** | `^0.8.20` |
| **Tujuan** | Melacak rantai pasok kopi dari panen hingga diterima |

## 2. Struktur Data

### 2.1 Enum `Statuskopi`

Mendefinisikan 4 tahap status kopi:

| Index | Nilai | Keterangan |
|-------|-------|------------|
| 0 | `panen` | Kopi baru dipanen |
| 1 | `Diproses` | Kopi sedang diproses |
| 2 | `Dikirim` | Kopi sedang dikirim |
| 3 | `Diterima` | Kopi telah diterima |

### 2.2 Struct `kopi`

| Field | Tipe | Keterangan |
|-------|------|------------|
| `id` | `uint256` | ID unik kopi |
| `namaPetani` | `string` | Nama petani pemanen |
| `beratKg` | `uint256` | Berat kopi dalam kilogram |
| `status` | `Statuskopi` | Status saat ini kopi |
| `pemilikSaatIni` | `address` | Alamat pemilik kopi saat ini |

### 2.3 State Variables

| Variable | Tipe | Visibility | Keterangan |
|----------|------|------------|------------|
| `totalkopi` | `uint256` | `public` | Counter total kopi terdaftar |
| `daftarKopi` | `mapping(uint256 => kopi)` | `public` | Mapping penyimpanan data kopi berdasarkan ID |

## 3. Fungsi

### 3.1 `daftarPemanenBaru`

```solidity
function daftarPemanenBaru(string memory _namaPetani, uint256 _beratKg) public
```

| Parameter | Tipe | Keterangan |
|-----------|------|-------------|
| `_namaPetani` | `string` | Nama petani |
| `_beratKg` | `uint256` | Berat hasil panen (kg) |

**Cara kerja:**
1. Increment `totalkopi` sebanyak 1.
2. Mendaftarkan data kopi baru ke `daftarKopi[totalkopi]` dengan:
   - `id` = `totalkopi`
   - `status` = `Statuskopi.panen`
   - `pemilikSaatIni` = `msg.sender` (alamat yang memanggil fungsi)

### 3.2 `updateStatus`

```solidity
function updateStatus(uint256 _id, Statuskopi _statusBaru) public
```

| Parameter | Tipe | Keterangan |
|-----------|------|-------------|
| `_id` | `uint256` | ID kopi yang ingin diubah |
| `_statusBaru` | `Statuskopi` | Status baru kopi |

**Validasi:**
1. `require(_id > 0 && _id <= totalkopi, "Kopi tidak ditemukan di sistem")` — memastikan ID kopi valid.
2. `require(msg.sender == daftarKopi[_id].pemilikSaatIni, "Anda tidak memiliki akses ...")` — hanya pemilik saat ini yang dapat mengubah status.

**Cara kerja:**
- Mengubah `daftarKopi[_id].status` menjadi `_statusBaru`.

## 4. Alur Rantai Pasok

```
panen → Diproses → Dikirim → Diterima
  (0)      (1)       (2)       (3)
```

1. **Panen** — Petani mendaftarkan hasil panen via `daftarPemanenBaru`.
2. **Diproses** — Pemilik mengubah status menjadi `Diproses`.
3. **Dikirim** — Pemilik mengubah status menjadi `Dikirim`.
4. **Diterima** — Pemilik mengubah status menjadi `Diterima`.

## 5. Keamanan

| Aspek | Status | Catatan |
|-------|--------|---------|
| Access Control | ✅ | Hanya `pemilikSaatIni` yang dapat `updateStatus` |
| Validasi ID | ✅ | `require` memastikan ID valid |
| Reentrancy | ✅ Aman | Tidak ada external call |
| Integer Overflow | ✅ Aman | Solidity ^0.8.20 punya built-in overflow check |

## 6. Saran Pengembangan

1. **Transfer kepemilikan** — Tambah fungsi untuk mengubah `pemilikSaatIni` agar rantai pasok bisa berpindah tangan.
2. **Event logging** — Tambah `event` untuk setiap perubahan status agar mudah dilacak off-chain.
3. **Modifier** — Gunakan `modifier onlyOwner(uint256 _id)` agar kode lebih bersih dan reusable.
4. **Batasan berat** — Tambah validasi `_beratKg > 0` pada `daftarPemanenBaru`.
5. **Timestamp** — Tambah field waktu panen dan waktu update status untuk audit trail.

## 7. Source Code Lengkap

```solidity
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.20 ;

contract SupplyChainKopi {
    enum Statuskopi { panen, Diproses, Dikirim, Diterima}
    struct kopi {
        uint256 id;
        string namaPetani;
        uint256 beratKg;
        Statuskopi status;
        address pemilikSaatIni;
    }
    uint256 public totalkopi = 0;
    mapping(uint256 => kopi) public daftarKopi;

    function daftarPemanenBaru(string memory _namaPetani, uint256 _beratKg) public {
        totalkopi += 1;

        daftarKopi[totalkopi] = kopi({
            id: totalkopi,
            namaPetani: _namaPetani,
            beratKg: _beratKg,
            status: Statuskopi.panen,
            pemilikSaatIni: msg.sender
        });
    }

    function updateStatus(uint256 _id, Statuskopi _statusBaru) public {
        require(_id > 0 && _id <= totalkopi, "Kopi tidak ditemukan di sistem");
        require(msg.sender == daftarKopi[_id].pemilikSaatIni, "Anda tidak memiliki akses untuk mengubah status kopi ini");
        daftarKopi[_id].status = _statusBaru;
    }
}
```

---

*Laporan dibuat dari file `/SupplyChainKopi.sol`*
