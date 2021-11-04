#include <list>
#include <vector>
#include <iostream>

using namespace std;

struct vertice {
    int posicaoLista;
    double preco;
    string nome;
};

typedef struct vertice Vertice;

class Grafo {

    private:
        int maximoVertices;
        int quantidadeVertices;
        bool *marcador;
        
        vector<Vertice> vertices;
        list<pair<string, int>> *listaAdjacencias;

    public:
        Grafo(int maximoVertices);

        bool insereVertice(string nome, double preco);
        bool insereAresta(string origem, string destino, int peso);
        void buscaLargura(Vertice origem, Vertice destino);
        void buscaProfundidade(Vertice origem, Vertice destino);
        void reiniciaMarcador();
        Vertice buscaVertice(string nomeVertice);
        void imprimirVertices();
        void imprimirListaAdjacencias();
};