db.createUser({
  user: "todoUser",
  pwd: "hakuna-matata-1672",
  roles: [
    {
      role: "readWrite",
      db: "solid-todo",
    },
  ],
});
