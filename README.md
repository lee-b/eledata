# Eledata

The `eledata` file format is a highly structured, elegant, and extensible data format, designed to be regular, readable, easily parsible, and to support arbitrary plugins.

In essence, it is a tree of abstract nodes, where each node is a type that your code defines.  The file format has JUST enough strucuture to support this, and no more.

The main purpose of `eledata` is to provide a strong, stable, elegant base on which to build `eledown`, a lightweight markup format.  However, eledata itself may also be useful as a general data file format, similar to json: especially for those who prefer dynamic, extensible, plugin-based trees of objects, rather than raw dictionaries or primitives.


## Basic Structure

The basic structure of an "eledown" document consists of curly-brace enclosed tags. A tag can have one more more arguments. Generally, all arguments are themselves curly-brace enclosed tags, which may have their own arguments, forever.

There are three built-in tags:

"text": A { text ... } tag treats all of its arguments as text values.

"literal": Takes one argument, which is a literal unicode character.

Additionally, there is one piece of syntactic sugar, for readability: if a tag only has one argument, you may omit the curly braces around that argument.  In this case, the ... argument is trtreated as { text ... }.

That's it.  That's the syntax of an `eledata` file!


# Examples

See examples/first.eld for an example of an `eledata` file (which might give some hints as to where I'm going with `eledown`, later):


This example file includes metadata about a document, as well as the document itself, including several sections with different types of content, such as paragraphs and images. Note that the tags used in this example document are just examples and do not represent any built-in tags or plugins in the "eledown" format.

##  Conclusion

The `eledata` format is a powerful and flexible way to create elegant, structured, readable, and extensible data files, with support for a wide range of content types and functionality through its plugins. Unlike file formats like json, its is not entirely "fixed", but provides a simple mechanism for endless extensions.  Also unlike json, it achives more with less syntax.

Finally, unlike markdown, it achieves simple, structured, elegant, readable files, that resemble the basic idea of latex more than the cumbersome so-called lightweight markup languages with myriad incompatibilies and hacked-on extra features like italics or tables with more and more weird syntax that's difficult to remember.  With eledata, it's simple and readable.  The intent is that eledown will be similarly elegant and readable.


## Contact 

mailto:leebraid@gmail.com

