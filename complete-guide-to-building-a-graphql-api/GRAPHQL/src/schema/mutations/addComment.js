import { GraphQLInt, GraphQLNonNull } from "graphql";
import { Comment, CommentInputType } from "../types/Comment";

import { fakeDatabase } from "../../FakeDatabase";

export default {
	addComment: {
		type: Comment,
		description: 'Creates a new comment for a blog post',
		args: { 
			comment: { type: CommentInputType }
		},
		resolve: function(parent, {comment} ) {
			return fakeDatabase.addNewComment(comment);
		}
	}
}