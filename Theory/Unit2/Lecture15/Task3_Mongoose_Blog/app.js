const mongoose = require("mongoose");

// Connect to MongoDB
mongoose
  .connect("mongodb://127.0.0.1:27017/blog_database")
  .then(() => {
    console.log("MongoDB connected successfully.");

    createPost()
      .then(() => {
        return readPosts();
      })
      .then(() => {
        return createComment();
      })
      .then(() => {
        return readComments();
      });
  })
  .catch((error) => {
    console.log("MongoDB connection error:", error);
  });

// Post schema
const postSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  content: {
    type: String,
    required: true,
  },
  author: {
    type: String,
    required: true,
  },
});

// Comment schema
const commentSchema = new mongoose.Schema({
  text: {
    type: String,
    required: true,
  },
  author: {
    type: String,
    required: true,
  },
  postId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Post",
    required: true,
  },
});

// Create models
const Post = mongoose.model("Post", postSchema);
const Comment = mongoose.model("Comment", commentSchema);

// Create a sample post
async function createPost() {
  const existingPost = await Post.findOne({
    title: "Introduction to Backend Development",
  });

  if (!existingPost) {
    const post = new Post({
      title: "Introduction to Backend Development",
      content:
        "Backend development handles server side logic and database interaction.",
      author: "Sehaj Vohra",
    });

    await post.save();

    console.log("Post created successfully.");
    console.log("Post ID:", post._id);
    console.log("Post Title:", post.title);
  } else {
    console.log("Post already exists.");
    console.log("Post ID:", existingPost._id);
  }
}

// Read posts
async function readPosts() {
  const posts = await Post.find();

  console.log("\nAll Posts:");

  posts.forEach((post) => {
    console.log("ID:", post._id);
    console.log("Title:", post.title);
    console.log("Author:", post.author);
    console.log("Content:", post.content);
  });
}

// Create a sample comment
async function createComment() {
  const post = await Post.findOne({
    title: "Introduction to Backend Development",
  });

  if (post) {
    const comment = new Comment({
      text: "This is a useful backend development post.",
      author: "Sehaj Vohra",
      postId: post._id,
    });

    await comment.save();

    console.log("\nComment created successfully.");
    console.log("Comment ID:", comment._id);
    console.log("Comment Text:", comment.text);
  }
}

async function readComments() {
  const comments = await Comment.find().populate("postId");

  console.log("\nAll Comments:");

  comments.forEach((comment) => {
    console.log("ID:", comment._id);
    console.log("Text:", comment.text);
    console.log("Author:", comment.author);
    console.log("Post:", comment.postId.title);
  });
}