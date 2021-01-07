import {FILE_PATH} from "../../config.js"

export default async ({response, request}) => {
	const decoder = new TextDecoder();
    const encoder = new TextEncoder();
    
	try{
        const r = await request.body();
        
        const val = await r.value
        const title = val.title;

        const data = await Deno.readFile(FILE_PATH);
        const todos = JSON.parse(decoder.decode(data));

        const newTodo = {id: todos.length + 1, title: title, completed: false};
        todos.push(newTodo);

        await Deno.writeFile(FILE_PATH, encoder.encode(JSON.stringify(todos)));

        response.status = 201;
        response.body = {status: "success", newTodo}
	} catch(err){
		console.log(err);
		response.status = 502;
		response.body = {status: "failed", error: err}
	}
}
