import {FILE_PATH} from "../../config.js"

export default async ({response, params}) => {
	const decoder = new TextDecoder();
    const encoder = new TextEncoder();
    
	try{

        const data = await Deno.readFile(FILE_PATH);
        const todos = JSON.parse(decoder.decode(data));

        const updatedTodos = todos.filter(todo => todo.id !== Number(params.id));

        await Deno.writeFile(FILE_PATH, encoder.encode(JSON.stringify(updatedTodos)));

        response.status = 200;
        response.body = {status: "success", todos: updatedTodos}
	} catch(err){
		console.log(err);
		response.status = 502;
		response.body = {status: "failed", error: err}
	}
}
