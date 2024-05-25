# AirBnB Clone - Web Static

Welcome to the AirBnB Clone project! In this phase of the project, we will be focusing on building the static front-end for our AirBnB clone. The goal is to create simple HTML pages with static content, which will later evolve into a fully functional web application.

## Project Overview

This project involves creating static web pages that will form the basis of our AirBnB clone. The main objectives are:

- To create HTML pages that structure our content appropriately.
- To apply CSS styling to these pages to make them visually appealing.
- To follow a style guide to ensure consistency across all pages.
- To use fake content as placeholders, since no data will be loaded from any sources.
- To avoid using Javascript at this stage.

## What You Will Learn

During this project, you will:

- Understand the basics of HTML and CSS.
- Learn how to structure HTML documents.
- Apply CSS styles to design web pages.
- Create and manage multiple HTML files.
- Prototype elements and pages effectively.

## Getting Started

### Prerequisites

Before you start, ensure you have forked or cloned the `AirBnB_clone` repository from your partner if you were not the owner of the previous project. This repository will serve as the base for your static web pages.

### Project Structure

Your project should be structured as follows:

```
AirBnB_clone/
├── images/
│   └── logo.png
├── styles/
│   └── main.css
├── index.html
├── about.html
└── contact.html
```

### Creating HTML Pages

Start by creating simple HTML pages. Here are a few example pages you might create:

1. **index.html**: The homepage of your AirBnB clone.
2. **about.html**: A page that describes your project or team.
3. **contact.html**: A page with contact information.

Each HTML page should have the basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles/main.css">
    <title>AirBnB Clone</title>
</head>
<body>
    <!-- Your content goes here -->
</body>
</html>
```

### Styling with CSS

Create a `styles/main.css` file where you will add your CSS rules. Here are some basic styles to get you started:

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #ff5a5f;
    color: white;
    padding: 1em;
    text-align: center;
}

footer {
    background-color: #333;
    color: white;
    padding: 1em;
    text-align: center;
    position: absolute;
    bottom: 0;
    width: 100%;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

img {
    max-width: 100%;
    height: auto;
}
```

### Placeholder Content

Since we are not loading any data, use placeholder content in your HTML files. This could be simple text, placeholder images, or dummy links.

```html
<div class="container">
    <h1>Welcome to AirBnB Clone</h1>
    <p>This is a prototype of our AirBnB clone project.</p>
    <img src="images/logo.png" alt="AirBnB Logo">
</div>
```

## Style Guide

- Use a consistent color scheme throughout your project.
- Stick to a single or complementary font families.
- Ensure your design is responsive and works on different screen sizes.
- Maintain a clean and organized folder structure.

## Conclusion

This project is a crucial step in building the front-end of your AirBnB clone. By the end of this phase, you will have a set of static HTML pages styled with CSS, providing a solid foundation for future development.

Happy coding!
