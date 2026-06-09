# Day 2 Notes

## Path Parameters

Used to identify a specific resource.

Example:

/users/1

user_id is extracted from the URL.

---

## Query Parameters

Used for filtering, searching, sorting, and pagination.

Example:

/users?page=2&limit=20

---

## Route Matching

Specific routes should come before dynamic routes.

Example:

/users/me

should be defined before

/users/{user_id}

---

## API Design Principle

URLs represent resources.

HTTP methods represent actions.