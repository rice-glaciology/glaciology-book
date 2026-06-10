# The labs

The chapters in the earlier parts of this book develop the physics of glaciers in words and equations. The chapters that follow turn that physics into computation. They are written as labs: self-contained exercises that you run yourself, change, and learn from by experiment.

Each lab builds a working model with icepack and uses it to illustrate a concept from the main text. The idea is to learn how ice flow behaves by making a model do it, rather than only by reading about it. Where a lab depends on a particular piece of theory, it points back to the chapter that covers it, so the labs and the main text are meant to be read together.

The labs assume you have the computing environment set up. Because icepack runs on Firedrake, which is awkward to install directly, the next chapter shows how to start a ready-made environment from the book's Docker image. Once that is running you can open any lab as a notebook and run it with the Firedrake kernel.

A note on what the labs are not. They are not executed when the book is built, because the modeling stack is too heavy to run on a documentation server. What you see on these pages is the code and an explanation of what it produces. To see the output, and to do the exercises at the end of each lab, you run the code in the container.

The labs are ordered so that each one adds a single piece of physics to a model you have already met. The first builds a floating ice shelf and solves for its velocity. Later labs add basal sliding, couple the flow to temperature, step the geometry forward in time, and bring in real data, so that by the end you have assembled a model that contains most of the processes covered in the main text.
