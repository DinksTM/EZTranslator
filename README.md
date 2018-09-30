# EZTranslator
Simple translation utility that writes to a file. That's all there is to it. There's support for both Linux (bash) and Windows (cmd), but no GUI because I'm lazy and this project is just a means to an end.

The origin file (aka what you are asked to translate from) is written in the form:

 ` A,`
  
  `B,`
  
  `C,`
  
And translated files are written in the form:

 ` OriginalA:TranslatedA,`
  
  `OriginalB:TranslatedB,`
  
  `OriginalC:TranslatedC,`
  
This is most useful for localising other projects.
