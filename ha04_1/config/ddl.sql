DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    status INTEGER DEFAULT 1
);

INSERT  INTO  posts (title, content) values ('post #1', 'It is very interesting post');
INSERT  INTO  posts (title, content) values ('post #2', 'Second post about HA 04');
INSERT  INTO  posts (title, content) values ('post #4', 'You can try to remove any post');
INSERT  INTO  posts (title, content) values ('Long post', 'Software development refers to a set of computer science activities dedicated to the process of creating, designing, deploying and supporting software.

Software itself is the set of instructions or programs that tell a computer what to do. It is independent of hardware and makes computers programmable. There are three basic types:

System software to provide core functions such as operating systems, disk management, utilities, hardware management and other operational necessities.

Programming software to give programmers tools such as text editors, compilers, linkers, debuggers and other tools to create code.

Application software (applications or apps) to help users perform tasks. Office productivity suites, data management software, media players and security programs are examples. Applications also refers to web and mobile applications like those used to shop on Amazon.com, socialize with Facebook or post pictures to Instagram');
