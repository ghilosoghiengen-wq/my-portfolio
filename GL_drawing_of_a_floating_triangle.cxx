#pragma comment(lib, "GLESv2")
#pragma comment(lib, "EGL")
#pragma comment(lib, "SDL2")

#include <iostream>
#include <SDL2/SDL.h>
#include <SDL2/SDL_opengles2.h>
#include <cmath>

// 1. شيدر النقاط والحركة (Vertex Shader)
const char* vertexShaderSource = 
    "attribute vec4 a_Position;    \n"
    "uniform float u_Time;         \n"
    "void main()                   \n"
    "{                             \n"
    "   vec4 pos = a_Position;     \n"
    "   pos.x += sin(u_Time + pos.y) * 0.05; \n" // محاكاة حركة مرونة قماش قميص دوبي
    "   gl_Position = pos;         \n"
    "}                             \n";

// 2. شيدر تلوين ملامح وفراء دوبي البني (Fragment Shader)
const char* fragmentShaderSource = 
    "precision mediump float;      \n"
    "void main()                   \n"
    "{                             \n"
    "   gl_FragColor = vec4(0.82, 0.41, 0.12, 1.0); \n" // لون فراء الدوبرمان (Tan)
    "}                             \n";

// 3. مصفوفة إحداثيات نقاط الجسد المبدئي (Vertices)
GLfloat dobbyVertices[] = {
     0.0f,  0.5f, 0.0f,  // الرأس الأعلى
    -0.4f, -0.4f, 0.0f,  // الكتف الأيسر
     0.4f, -0.4f, 0.0f   // الكتف الأيمن
};

int main(int argc, char* argv[]) {
    std::cout << "بدء تشغيل المحرك بعد إعادة التثبيت النظيفة..." << std::endl;

    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "فشل SDL: " << SDL_GetError() << std::endl;
        return -1;
    }

    SDL_Window* window = SDL_CreateWindow("Dobie Clean Engine", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 400, SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN);
    if (!window) return -1;

    SDL_GLContext glContext = SDL_GL_CreateContext(window);

    // بناء وتجميع الشيدر داخل كارت الشاشة
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vertexShader);

    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);

    GLuint program = glCreateProgram();
    glAttachShader(program, vertexShader);
    glAttachShader(program, fragmentShader);
    glLinkProgram(program);
    glUseProgram(program);

    GLuint posLoc = glGetAttribLocation(program, "a_Position");
    GLuint timeLoc = glGetUniformLocation(program, "u_Time");

    glEnableVertexAttribArray(posLoc);
    glVertexAttribPointer(posLoc, 3, GL_FLOAT, GL_FALSE, 0, dobbyVertices);

    // 4. حلقة اللعبة النشطة (Game Loop)
    bool running = true;
    SDL_Event event;
    float timeCounter = 0.0f;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) running = false;
        }

        timeCounter += 0.05f; // تحديث الوقت لتفعيل فيزياء حركة الملابس
        glUniform1f(timeLoc, timeCounter);

        // تنظيف الشاشة باللون الكحلي لبدلة الشرطة
        glClearColor(0.0f, 0.11f, 0.38f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        // أمر الرسم الفعلي للمجسم
        glDrawArrays(GL_TRIANGLES, 0, 3);

        SDL_GL_SwapWindow(window);
        SDL_Delay(16); // الحفاظ على أداء 60 إطار في الثانية
    }

    SDL_GL_DeleteContext(glContext);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
