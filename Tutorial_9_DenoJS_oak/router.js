import { Router } from "https://deno.land/x/oak/mod.ts";

import getTodos from './controllers/todos/get.js'
import postTodos from './controllers/todos/post.js'
import deleteTodos from './controllers/todos/delete.js'
import putTodos from './controllers/todos/put.js'

const router = new Router();

router.get("/", ({response}) => {
  response.body = "Todo List Api Using Deno Runtime.";
});


router
  .get("/todos", getTodos)
  .post("/todos", postTodos)
  .delete("/todos/:id", deleteTodos)
  .put("/todos/:id", putTodos);

export default router;
