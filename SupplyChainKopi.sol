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
    daftarKopi[_id] .status = _statusBaru;

}
}