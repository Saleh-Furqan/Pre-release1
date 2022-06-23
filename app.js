let userDatabase = [];
let jTeamMemb = 0;
let aTeamMemb = 0;
let sTeamMemb = 0;
let gTeamMemb = 0;

let users = [];

const User = (name, age, gender, typeMemb, isTeamMemb, annualFee, feePaid) => {
	return { name, age, gender, typeMemb, isTeamMemb, annualFee, feePaid };
};

const addUsers = (user) => {
	const list = document.querySelector(".list");
	const row = document.createElement("tr");
	row.innerHTML = `
    <td>${user.name}</td>
    <td>${user.age}</td>
    <td>${user.gender}</td>
    <td>${user.typeMemb}</td>
    <td>${user.isTeamMemb}</td>
    <td>${user.annualFee}</td>
    <td>${user.feePaid}</td>
    <td><button class="deleteRow"">X</button></td>
    `;
	list.appendChild(row);
};

const displayUsers = () => {
	let users = getUsers();
	users.forEach((user) => {
		addUsers(user);
	});
};
// displayUsers();

const clearFields = () => {
	inputs = document.querySelectorAll(".inputs");
	inputs.forEach((input) => {
		input.value = "";
	});
	// document.querySelector(".age").value = "";
	// document.querySelectorAll(".gender").value = "";
	// document.querySelectorAll(".isTeamMember").value = "";
	// document.querySelectorAll(".didUserPay").value = "";
};

function saveUser(x) {
	users.push(x);
}
const deleteUser = (e) => {
	if (e.classList.contains("deleteRow")) {
		e.parentElement.parentElement.remove();
	}
};

document.querySelector("[data-form]").addEventListener("submit", (e) => {
	e.preventDefault();

	const name = document.querySelector(".name").value;

	const age = document.querySelector(".age").value;
	const typeMemb = validAge()[0];
	const annualFee = validAge()[1];
	function validAge() {
		let typeMemb;
		let annualFee;
		if (age < 18 && age >= 2) {
			typeMemb = "junior";
			annualFee = 10;
			return [typeMemb, annualFee];
		} else if (age < 50 && age >= 18) {
			typeMemb = "adult";
			annualFee = 20;
			return [typeMemb, annualFee];
		} else if (age < 80 && age >= 50) {
			typeMemb = "senior";
			annualFee = 15;
			return [typeMemb, annualFee];
		} else if (age >= 80) {
			typeMemb = "golden";
			annualFee = 0;
			return [typeMemb, annualFee];
		}
	}

	const gender = validGender();
	function validGender() {
		let gender;
		if (
			!document.querySelector("#male").checked &&
			!document.querySelector("#female").checked
		) {
			return;
		} else if (
			document.querySelector("#male").checked &&
			!document.querySelector("#female").checked
		) {
			gender = "male";
			return gender;
		} else if (
			document.querySelector("#female").checked &&
			!document.querySelector("#male").checked
		) {
			gender = "female";
			return gender;
		}
	}

	const isTeamMemb = validMember();
	function validMember() {
		let read;
		if (
			!document.querySelector("#isTeamMember").checked &&
			!document.querySelector("#notTeamMember").checked
		) {
			return;
		} else if (
			document.querySelector("#isTeamMember").checked &&
			!document.querySelector("#notTeamMember").checked
		) {
			read = "team member";
			return read;
		} else if (
			document.querySelector("#notTeamMember").checked &&
			!document.querySelector("#isTeamMember").checked
		) {
			read = "not team member";
			return read;
		}
	}

	const feePaid = validPaid();
	function validPaid() {
		let read;
		if (
			!document.querySelector("#paid").checked &&
			!document.querySelector("#notPaid").checked
		) {
			return;
		} else if (
			document.querySelector("#paid").checked &&
			!document.querySelector("#notPaid").checked
		) {
			read = "paid";
			return read;
		} else if (
			document.querySelector("#notPaid").checked &&
			!document.querySelector("#paid").checked
		) {
			read = "not paid";
			return read;
		}
	}

	if (
		name === "" ||
		age === "" ||
		gender === "" ||
		isTeamMemb === "" ||
		feePaid === ""
	) {
		return;
	} else {
		const user = User(
			name,
			age,
			gender,
			typeMemb,
			isTeamMemb,
			annualFee,
			feePaid
		);
		addUsers(user);
		saveUser(user);
		clearFields();
	}
});

document.querySelector(".list").addEventListener("click", (e) => {
	deleteUser(e.target);
});
