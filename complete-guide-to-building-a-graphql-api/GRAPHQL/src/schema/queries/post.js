import { GraphQLInt, GraphQLNonNull } from "graphql";
import { Post } from "../types/Post";
import { fakeDatabase } from "../../FakeDatabase";

export default {
	post: {
		type: Post,
		description: 'Get details about a specific post',
		args: { 
			id: { type: new GraphQLNonNull(GraphQLInt) }
		},
		resolve: function(parent, {id} ) {
			return fakeDatabase.getBlogPost(id);
		}
	}
}